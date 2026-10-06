# 4. Items y Pipelines

Hasta ahora vimos spiders que devuelven diccionarios sueltos (`yield {"titulo": ...}`). Funciona, pero para proyectos serios conviene **estructurar** los datos con `Item` y **procesarlos** con pipelines antes de guardarlos.

## 4.1. Definir un Item

En `items.py`:

```python
import scrapy

class LibroItem(scrapy.Item):
    titulo = scrapy.Field()
    precio = scrapy.Field()
    disponibilidad = scrapy.Field()
    rating = scrapy.Field()
    url = scrapy.Field()
```

Uso en el spider:

```python
from miproyecto.items import LibroItem

class LibrosSpider(scrapy.Spider):
    name = "libros"
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for libro in response.css("article.product_pod"):
            item = LibroItem()
            item["titulo"] = libro.css("h3 a::attr(title)").get()
            item["precio"] = libro.css("p.price_color::text").get()
            item["url"] = response.urljoin(libro.css("h3 a::attr(href)").get())
            yield item
```

### ¿Por qué usar Item en vez de un dict simple?

- **Validación de estructura**: si intentás asignar un campo que no definiste, Scrapy lanza un error (`KeyError`), lo cual ayuda a detectar typos temprano.
- **Documentación implícita**: cualquiera que abra `items.py` ve exactamente qué campos produce el proyecto.
- Se integra mejor con **pipelines**, **exporters**, e **ItemLoaders**.

### Alternativa moderna: `dataclass` o `attrs`

Desde versiones recientes, Scrapy también soporta usar `dataclasses` estándar de Python en vez de `scrapy.Item`:

```python
from dataclasses import dataclass

@dataclass
class LibroItem:
    titulo: str
    precio: str
    url: str
```

Esto es útil si ya estás familiarizado con dataclasses y querés type hints nativos.

## 4.2. ItemLoader: cargar y limpiar datos de forma declarativa

Cuando la extracción de cada campo requiere limpieza (strip, conversión de tipo, valores por defecto), escribir todo eso a mano en el spider se vuelve repetitivo. `ItemLoader` permite declarar esa lógica una sola vez.

```python
# items.py
import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join

def limpiar_precio(valor):
    return valor.replace("£", "").strip()

class LibroItem(scrapy.Item):
    titulo = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
    )
    precio = scrapy.Field(
        input_processor=MapCompose(limpiar_precio, float),
        output_processor=TakeFirst(),
    )
    descripcion = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=Join(" "),
    )
```

```python
# spider
from scrapy.loader import ItemLoader
from miproyecto.items import LibroItem

def parse(self, response):
    for libro in response.css("article.product_pod"):
        loader = ItemLoader(item=LibroItem(), selector=libro)
        loader.add_css("titulo", "h3 a::attr(title)")
        loader.add_css("precio", "p.price_color::text")
        yield loader.load_item()
```

- `input_processor`: se aplica a cada valor extraído individualmente (ej. limpiar cada string).
- `output_processor`: se aplica al final, sobre la **lista** de valores extraídos, para decidir el valor final del campo (ej. `TakeFirst()` toma solo el primero, `Join()` los une en un string).

Esto separa claramente la lógica de "cómo extraer" (en el spider) de "cómo limpiar/normalizar" (en el item), lo cual es más mantenible en proyectos grandes.

## 4.3. Item Pipelines

Los pipelines procesan cada item **después** de que el spider lo genera, y **antes** de exportarlo. Casos de uso típicos:

- Validar datos (descartar items incompletos).
- Limpiar/normalizar datos.
- Detectar y filtrar duplicados.
- Guardar en una base de datos.
- Descargar imágenes o archivos asociados.

### Estructura básica de un pipeline

```python
# pipelines.py

class ValidarPrecioPipeline:
    def process_item(self, item, spider):
        if not item.get("precio"):
            raise DropItem(f"Item sin precio: {item}")
        return item
```

```python
from scrapy.exceptions import DropItem

class ValidarPrecioPipeline:
    def process_item(self, item, spider):
        if not item.get("precio"):
            raise DropItem(f"Item sin precio: {item}")
        return item
```

`DropItem` descarta el item, y ese item no continúa al siguiente pipeline ni se exporta.

### Pipeline para filtrar duplicados

```python
class DuplicadosPipeline:
    def __init__(self):
        self.urls_vistas = set()

    def process_item(self, item, spider):
        if item["url"] in self.urls_vistas:
            raise DropItem(f"Item duplicado: {item['url']}")
        self.urls_vistas.add(item["url"])
        return item
```

### Pipeline para guardar en base de datos (ejemplo con SQLite)

```python
import sqlite3

class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect("libros.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                titulo TEXT, precio TEXT, url TEXT
            )
        """)

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.cursor.execute(
            "INSERT INTO libros (titulo, precio, url) VALUES (?, ?, ?)",
            (item["titulo"], item["precio"], item["url"]),
        )
        self.conn.commit()
        return item
```

`open_spider` y `close_spider` son hooks que se ejecutan al iniciar/terminar el crawling — ideales para abrir/cerrar conexiones.

### Activar los pipelines

Los pipelines definidos no se ejecutan automáticamente: hay que registrarlos en `settings.py` con un número de prioridad (menor número = se ejecuta primero):

```python
# settings.py
ITEM_PIPELINES = {
    "miproyecto.pipelines.ValidarPrecioPipeline": 100,
    "miproyecto.pipelines.DuplicadosPipeline": 200,
    "miproyecto.pipelines.SQLitePipeline": 300,
}
```

## 4.4. Pipeline para descargar imágenes o archivos

Scrapy trae pipelines integrados para descargar imágenes y archivos automáticamente:

```python
# settings.py
ITEM_PIPELINES = {
    "scrapy.pipelines.images.ImagesPipeline": 1,
}
IMAGES_STORE = "imagenes_descargadas"
```

```python
# items.py
class LibroItem(scrapy.Item):
    titulo = scrapy.Field()
    image_urls = scrapy.Field()   # nombre requerido por defecto
    images = scrapy.Field()        # resultado poblado automáticamente
```

```python
# spider
def parse(self, response):
    for libro in response.css("article.product_pod"):
        yield {
            "titulo": libro.css("h3 a::attr(title)").get(),
            "image_urls": [response.urljoin(libro.css("img::attr(src)").get())],
        }
```

Scrapy descarga las imágenes automáticamente, evita duplicados por hash de contenido, y genera miniaturas si se configura.

## Siguiente paso

Ya vimos cómo estructurar y procesar los datos extraídos. Ahora veamos cómo navegar sitios más complejos: paginación, formularios y APIs. Continuá con **[05-requests-avanzado.md](05-requests-avanzado.md)**.
