# 10. Ejemplos prácticos completos

Todos los ejemplos usan [books.toscrape.com](https://books.toscrape.com) y [quotes.toscrape.com](https://quotes.toscrape.com), sitios creados específicamente para practicar scraping sin implicancias legales ni éticas.

## 10.1. Catálogo completo de productos con paginación

Spider completo que recorre **todas** las páginas del catálogo, extrayendo datos estructurados de cada libro.

```python
# spiders/catalogo_completo.py
import scrapy

class CatalogoCompletoSpider(scrapy.Spider):
    name = "catalogo_completo"
    start_urls = ["https://books.toscrape.com"]

    custom_settings = {
        "DOWNLOAD_DELAY": 0.5,
        "AUTOTHROTTLE_ENABLED": True,
    }

    def parse(self, response):
        for libro in response.css("article.product_pod"):
            url_detalle = libro.css("h3 a::attr(href)").get()
            yield response.follow(url_detalle, callback=self.parse_detalle)

        siguiente = response.css("li.next a::attr(href)").get()
        if siguiente:
            yield response.follow(siguiente, callback=self.parse)

    def parse_detalle(self, response):
        rating_texto = response.css("p.star-rating::attr(class)").get() or ""
        rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating_num = next(
            (v for k, v in rating_map.items() if k in rating_texto), None
        )

        tabla = {}
        for fila in response.css("table.table-striped tr"):
            clave = fila.css("th::text").get()
            valor = fila.css("td::text").get()
            if clave and valor:
                tabla[clave] = valor

        yield {
            "titulo": response.css("h1::text").get(),
            "precio": response.css("p.price_color::text").get(),
            "disponibilidad": response.css("p.availability::text").getall()[-1].strip(),
            "rating": rating_num,
            "descripcion": (
                response.css("#product_description ~ p::text").get() or ""
            ).strip(),
            "upc": tabla.get("UPC"),
            "url": response.url,
        }
```

```bash
scrapy crawl catalogo_completo -o catalogo.jsonl
```

## 10.2. Spider con login (autenticación)

Ejemplo usando `quotes.toscrape.com/login`, que también está pensado para practicar:

```python
# spiders/citas_logueado.py
import scrapy

class CitasLogueadoSpider(scrapy.Spider):
    name = "citas_logueado"
    start_urls = ["https://quotes.toscrape.com/login"]

    def parse(self, response):
        # El formulario tiene un token CSRF que se completa automáticamente
        yield scrapy.FormRequest.from_response(
            response,
            formdata={"username": "admin", "password": "admin"},
            callback=self.tras_login,
        )

    def tras_login(self, response):
        if "Logout" not in response.text:
            self.logger.error("Login falló, revisá las credenciales")
            return

        yield response.follow("https://quotes.toscrape.com", callback=self.parse_citas)

    def parse_citas(self, response):
        for cita in response.css("div.quote"):
            yield {
                "texto": cita.css("span.text::text").get(),
                "autor": cita.css("small.author::text").get(),
                "tags": cita.css("a.tag::text").getall(),
            }

        siguiente = response.css("li.next a::attr(href)").get()
        if siguiente:
            yield response.follow(siguiente, callback=self.parse_citas)
```

## 10.3. Proyecto completo con Items, ItemLoader y Pipeline de base de datos

### `items.py`

```python
import scrapy
from itemloaders.processors import TakeFirst, MapCompose

def limpiar_precio(valor):
    return valor.replace("£", "").strip()

def a_float(valor):
    try:
        return float(valor)
    except (TypeError, ValueError):
        return None

class LibroItem(scrapy.Item):
    titulo = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
    )
    precio = scrapy.Field(
        input_processor=MapCompose(limpiar_precio, a_float),
        output_processor=TakeFirst(),
    )
    url = scrapy.Field(output_processor=TakeFirst())
```

### `spiders/libros_loader.py`

```python
import scrapy
from scrapy.loader import ItemLoader
from miproyecto.items import LibroItem

class LibrosLoaderSpider(scrapy.Spider):
    name = "libros_loader"
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for libro in response.css("article.product_pod"):
            loader = ItemLoader(item=LibroItem(), selector=libro)
            loader.add_css("titulo", "h3 a::attr(title)")
            loader.add_css("precio", "p.price_color::text")
            loader.add_value("url", response.urljoin(libro.css("h3 a::attr(href)").get()))
            yield loader.load_item()

        siguiente = response.css("li.next a::attr(href)").get()
        if siguiente:
            yield response.follow(siguiente, callback=self.parse)
```

### `pipelines.py`

```python
from scrapy.exceptions import DropItem
import sqlite3

class ValidarPipeline:
    def process_item(self, item, spider):
        if item.get("precio") is None:
            raise DropItem(f"Sin precio válido: {item}")
        return item

class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect("libros.db")
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                titulo TEXT, precio REAL, url TEXT UNIQUE
            )
        """)

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        try:
            self.conn.execute(
                "INSERT OR IGNORE INTO libros (titulo, precio, url) VALUES (?, ?, ?)",
                (item["titulo"], item["precio"], item["url"]),
            )
        except sqlite3.Error as e:
            spider.logger.error(f"Error guardando en DB: {e}")
        return item
```

### `settings.py` (fragmento relevante)

```python
ITEM_PIPELINES = {
    "miproyecto.pipelines.ValidarPipeline": 100,
    "miproyecto.pipelines.SQLitePipeline": 300,
}
ROBOTSTXT_OBEY = True
AUTOTHROTTLE_ENABLED = True
DOWNLOAD_DELAY = 0.5
```

## 10.4. Consumir una API JSON paginada

```python
# spiders/api_citas.py
import scrapy

class ApiCitasSpider(scrapy.Spider):
    name = "api_citas"

    def start_requests(self):
        yield scrapy.Request(
            "https://quotes.toscrape.com/api/quotes?page=1",
            callback=self.parse_api,
        )

    def parse_api(self, response):
        data = response.json()

        for cita in data.get("quotes", []):
            yield {
                "texto": cita.get("text"),
                "autor": cita.get("author", {}).get("name"),
                "tags": cita.get("tags"),
            }

        if data.get("has_next"):
            siguiente_pagina = data["page"] + 1
            yield scrapy.Request(
                f"https://quotes.toscrape.com/api/quotes?page={siguiente_pagina}",
                callback=self.parse_api,
            )
```

## 10.5. Spider con reintentos personalizados y manejo robusto de errores

```python
import scrapy
from twisted.internet.error import TimeoutError, ConnectionRefusedError

class RobustoSpider(scrapy.Spider):
    name = "robusto"
    start_urls = ["https://books.toscrape.com"]

    custom_settings = {
        "RETRY_TIMES": 5,
        "RETRY_HTTP_CODES": [500, 502, 503, 504, 408, 429],
        "DOWNLOAD_TIMEOUT": 10,
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                callback=self.parse,
                errback=self.manejar_error,
                dont_filter=True,
            )

    def parse(self, response):
        for libro in response.css("article.product_pod"):
            yield {"titulo": libro.css("h3 a::attr(title)").get()}

    def manejar_error(self, failure):
        request = failure.request
        if failure.check(TimeoutError):
            self.logger.warning(f"Timeout: {request.url}")
        elif failure.check(ConnectionRefusedError):
            self.logger.warning(f"Conexión rechazada: {request.url}")
        else:
            self.logger.error(f"Error inesperado en {request.url}: {failure.value}")
```

## 10.6. Ejecutar todo desde un script Python (sin CLI)

```python
# ejecutar.py
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from miproyecto.spiders.catalogo_completo import CatalogoCompletoSpider

settings = get_project_settings()
settings.set("FEEDS", {"catalogo.json": {"format": "json", "encoding": "utf8"}})

process = CrawlerProcess(settings)
process.crawl(CatalogoCompletoSpider)
process.start()
```

```bash
python ejecutar.py
```

## Resumen final

- Empezá siempre por el **shell de Scrapy** (`scrapy shell`) para probar selectores antes de escribir el spider completo.
- Estructurá los datos con **Items** y limpialos con **ItemLoaders**/**Pipelines** en vez de manipular todo dentro del spider.
- Usá `response.follow()` para paginación y crawling, y `cb_kwargs` para pasar datos entre callbacks.
- Activá `AUTOTHROTTLE_ENABLED` y respetá `robots.txt` — es mejor un scraping lento y sostenible que uno agresivo que termina bloqueado.
- Si el sitio depende de JavaScript, integrá `scrapy-playwright` solo donde haga falta.
- Revisá siempre `robots.txt` y los Términos de Servicio antes de scrapear un sitio real (ver `09-buenas-practicas-legales.md`).
