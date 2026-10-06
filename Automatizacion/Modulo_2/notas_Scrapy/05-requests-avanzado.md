# 5. Requests avanzado: paginación, formularios y APIs

## 5.1. Seguir enlaces (crawling)

La forma más simple de seguir un enlace desde una página es con `response.follow()`, que maneja automáticamente URLs relativas (a diferencia de `scrapy.Request` puro, donde hay que resolver la URL vos mismo):

```python
def parse(self, response):
    for libro in response.css("article.product_pod"):
        yield {"titulo": libro.css("h3 a::attr(title)").get()}

    siguiente_pagina = response.css("li.next a::attr(href)").get()
    if siguiente_pagina is not None:
        yield response.follow(siguiente_pagina, callback=self.parse)
```

Este patrón — extraer datos y, si hay página siguiente, volver a llamar al mismo `parse` — es el más común para **paginación**.

### `response.follow()` también acepta un selector directamente

```python
yield response.follow(response.css("li.next a"), callback=self.parse)
```

### Seguir múltiples enlaces con `follow_all`

```python
yield from response.follow_all(css="a.categoria", callback=self.parse_categoria)
```

## 5.2. Callbacks distintos para distintos tipos de página

Es común tener un callback para la página de listado y otro para la página de detalle de cada producto:

```python
def parse(self, response):
    # página de listado
    for libro in response.css("article.product_pod"):
        url_detalle = libro.css("h3 a::attr(href)").get()
        yield response.follow(url_detalle, callback=self.parse_detalle)

    siguiente = response.css("li.next a::attr(href)").get()
    if siguiente:
        yield response.follow(siguiente, callback=self.parse)

def parse_detalle(self, response):
    yield {
        "titulo": response.css("h1::text").get(),
        "descripcion": response.css("div#product_description ~ p::text").get(),
        "precio": response.css("p.price_color::text").get(),
        "url": response.url,
    }
```

## 5.3. Pasar datos entre callbacks con `cb_kwargs`

A veces necesitás pasar datos extraídos en una página a la función que procesa la siguiente (por ejemplo, la categoría del listado, que no aparece en la página de detalle):

```python
def parse(self, response):
    categoria = response.css("h1::text").get()
    for libro in response.css("article.product_pod"):
        url_detalle = libro.css("h3 a::attr(href)").get()
        yield response.follow(
            url_detalle,
            callback=self.parse_detalle,
            cb_kwargs={"categoria": categoria},
        )

def parse_detalle(self, response, categoria):
    yield {
        "titulo": response.css("h1::text").get(),
        "categoria": categoria,
    }
```

`cb_kwargs` es la forma moderna recomendada (reemplaza al uso más antiguo de `meta` para este propósito, aunque `meta` sigue siendo válido para otros usos como configurar proxies o desactivar cookies por request).

## 5.4. `meta`: metadata a nivel de request

`meta` es un diccionario general para pasar información asociada a una request, disponible después en `response.meta`. Se usa tanto para pasar datos propios como para configurar el comportamiento de Scrapy en esa request puntual:

```python
yield scrapy.Request(
    url,
    callback=self.parse_detalle,
    meta={
        "proxy": "http://mi-proxy:8000",
        "dont_retry": True,
        "download_timeout": 10,
    },
)
```

```python
def parse_detalle(self, response):
    proxy_usado = response.meta.get("proxy")
```

## 5.5. Enviar formularios con `FormRequest`

Para sitios que requieren enviar un formulario (por ejemplo, un login o un buscador):

```python
import scrapy

class LoginSpider(scrapy.Spider):
    name = "login"
    start_urls = ["https://ejemplo.com/login"]

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={"usuario": "mi_usuario", "password": "mi_password"},
            callback=self.tras_login,
        )

    def tras_login(self, response):
        if "Cerrar sesión" in response.text:
            self.logger.info("Login exitoso")
        else:
            self.logger.error("Login falló")
```

`FormRequest.from_response()` es especialmente útil porque **detecta automáticamente** el formulario en la página y completa los campos ocultos (tokens CSRF, etc.), sumando solo los campos que vos especificás en `formdata`.

### Formulario de búsqueda simple

```python
yield scrapy.FormRequest(
    url="https://ejemplo.com/buscar",
    formdata={"q": "python scraping"},
    callback=self.parse_resultados,
)
```

## 5.6. Consumir APIs JSON directamente

Muchos sitios modernos cargan datos vía APIs internas en formato JSON (se pueden detectar inspeccionando la pestaña "Network" del navegador). Cuando es así, **conviene atacar la API directamente en vez del HTML** — es más rápido, más estable y más fácil de parsear:

```python
import scrapy
import json

class ApiSpider(scrapy.Spider):
    name = "api_ejemplo"

    def start_requests(self):
        yield scrapy.Request(
            "https://ejemplo.com/api/productos?page=1",
            callback=self.parse_api,
        )

    def parse_api(self, response):
        data = json.loads(response.text)
        for producto in data["resultados"]:
            yield {
                "nombre": producto["nombre"],
                "precio": producto["precio"],
            }

        if data.get("siguiente_pagina"):
            yield scrapy.Request(
                data["siguiente_pagina"],
                callback=self.parse_api,
            )
```

También podés acceder al JSON parseado directamente con `response.json()` (disponible desde versiones recientes de Scrapy), sin necesidad de importar `json`:

```python
def parse_api(self, response):
    data = response.json()
    ...
```

## 5.7. `start_requests()`: personalizar las requests iniciales

Si necesitás más control sobre las requests iniciales que el que permite `start_urls` (por ejemplo, agregar headers, cookies, o hacer un POST inicial), sobreescribí `start_requests()`:

```python
class MiSpider(scrapy.Spider):
    name = "mi_spider"

    def start_requests(self):
        urls = ["https://ejemplo.com/pagina1", "https://ejemplo.com/pagina2"]
        for url in urls:
            yield scrapy.Request(
                url,
                callback=self.parse,
                headers={"User-Agent": "Mi Bot 1.0"},
            )
```

## 5.8. Prioridad de requests

Cuando hay muchas URLs en cola, se puede controlar el orden de procesamiento con `priority` (mayor número = mayor prioridad, se procesa antes):

```python
yield scrapy.Request(url, callback=self.parse, priority=10)
```

Esto es útil, por ejemplo, para priorizar páginas de detalle sobre páginas de listado adicionales, o para implementar una estrategia de crawling en profundidad (`DFS`) vs en anchura (`BFS`) — Scrapy usa BFS por defecto (LIFO/FIFO configurable vía `DEPTH_PRIORITY` en settings).

## 5.9. Limitar la profundidad del crawling

```python
# settings.py
DEPTH_LIMIT = 3   # no seguir más de 3 niveles de enlaces desde start_urls
```

## 5.10. `CrawlSpider`: crawling basado en reglas

Para sitios donde el patrón de navegación es repetitivo (por ejemplo, "seguir todos los enlaces que matcheen tal patrón, y en cada uno extraer datos con tal otra regla"), `CrawlSpider` permite declarar esto de forma más compacta que escribir la lógica de seguimiento a mano:

```python
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MiCrawlSpider(CrawlSpider):
    name = "crawl_ejemplo"
    allowed_domains = ["ejemplo.com"]
    start_urls = ["https://ejemplo.com"]

    rules = (
        # Seguir enlaces de categorías, sin extraer nada de ellos (solo navegar)
        Rule(LinkExtractor(allow=r"/categoria/")),

        # Seguir enlaces de producto y extraer datos con parse_producto
        Rule(LinkExtractor(allow=r"/producto/\d+"), callback="parse_producto"),
    )

    def parse_producto(self, response):
        yield {
            "titulo": response.css("h1::text").get(),
            "precio": response.css("span.precio::text").get(),
        }
```

**Importante:** en `CrawlSpider`, nunca se sobreescribe el método `parse` (está reservado internamente para el manejo de las reglas) — hay que usar otros nombres de callback como `parse_producto`.

## Siguiente paso

Para casos como rotar proxies, user-agents, manejar cookies avanzadas o reintentos personalizados, seguí con **[06-middlewares.md](06-middlewares.md)**.
