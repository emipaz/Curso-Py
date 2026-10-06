# 2. Primeros pasos

## 2.1. Crear un proyecto

Scrapy organiza el trabajo en "proyectos", que generan una estructura de carpetas estándar:

```bash
scrapy startproject miproyecto
```

Esto crea:

```
miproyecto/
├── scrapy.cfg
└── miproyecto/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders/
        └── __init__.py
```

- **`scrapy.cfg`**: archivo de configuración de despliegue (define qué settings usar).
- **`items.py`**: donde definís la estructura de los datos que vas a extraer.
- **`middlewares.py`**: middlewares personalizados (proxies, headers, etc.).
- **`pipelines.py`**: procesamiento posterior de los items extraídos (limpieza, guardado en DB).
- **`settings.py`**: configuración global del proyecto (concurrencia, delays, user-agent, etc.).
- **`spiders/`**: carpeta donde van todos tus spiders (las clases que definen qué scrapear).

## 2.2. Generar un spider

```bash
cd miproyecto
scrapy genspider libros books.toscrape.com
```

Esto crea `spiders/libros.py` con una plantilla básica:

```python
import scrapy

class LibrosSpider(scrapy.Spider):
    name = "libros"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
```

- **`name`**: identificador único del spider (se usa para ejecutarlo con `scrapy crawl <name>`).
- **`allowed_domains`**: lista de dominios permitidos; Scrapy descarta automáticamente requests a otros dominios (útil como salvaguarda contra loops infinitos siguiendo enlaces externos).
- **`start_urls`**: URLs iniciales por donde arranca el crawling.
- **`parse`**: método callback que se ejecuta con la respuesta de cada URL en `start_urls`. Acá es donde extraés datos y/o generás nuevas requests.

## 2.3. Tu primer spider funcional

Vamos a scrapear un sitio de práctica pensado para esto: [books.toscrape.com](https://books.toscrape.com), que simula una librería online.

```python
# spiders/libros.py
import scrapy

class LibrosSpider(scrapy.Spider):
    name = "libros"
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for libro in response.css("article.product_pod"):
            yield {
                "titulo": libro.css("h3 a::attr(title)").get(),
                "precio": libro.css("p.price_color::text").get(),
                "disponibilidad": libro.css("p.instock.availability::text").get(default="").strip(),
                "rating": libro.css("p.star-rating::attr(class)").get(),
            }
```

Puntos clave:

- `response.css(...)` selecciona elementos usando selectores CSS (ver `03-selectores.md` en detalle).
- `yield` (no `return`) porque un spider puede generar múltiples items (y también requests) — Scrapy los procesa como un generador.
- `.get()` extrae el primer resultado que matchea el selector; `.getall()` extrae todos como lista.

## 2.4. Ejecutar el spider

```bash
scrapy crawl libros
```

Esto imprime en consola un log detallado (requests hechas, items extraídos, estadísticas finales) además de los datos extraídos si no se especifica archivo de salida.

### Guardar los resultados

```bash
scrapy crawl libros -o resultados.json
scrapy crawl libros -o resultados.csv
scrapy crawl libros -o resultados.jsonl   # JSON Lines, un item por línea
scrapy crawl libros -o resultados.xml
```

Scrapy detecta el formato automáticamente por la extensión del archivo. También soporta exportar directamente a S3, FTP, o Google Cloud Storage con la sintaxis `-o s3://bucket/archivo.json` (requiere configuración adicional de credenciales).

Para **agregar** a un archivo existente en vez de sobreescribir:

```bash
scrapy crawl libros -o resultados.json:jsonlines -t jsonlines
```

O más simple, usando `-O` (mayúscula) para sobreescribir siempre, y `-o` (minúscula) para agregar:

```bash
scrapy crawl libros -O resultados.json    # sobreescribe
scrapy crawl libros -o resultados.json    # agrega (append)
```

## 2.5. Scrapy shell: probar selectores interactivamente

Antes de escribir el spider completo, es muy útil probar los selectores CSS/XPath de forma interactiva con el **shell** de Scrapy:

```bash
scrapy shell "https://books.toscrape.com"
```

Esto abre una consola Python con la respuesta ya descargada, disponible en la variable `response`:

```python
>>> response.css("article.product_pod")
>>> response.css("h3 a::attr(title)").get()
'A Light in the Attic'
>>> response.css("h3 a::attr(title)").getall()
['A Light in the Attic', 'Tipping the Velvet', ...]
>>> response.url
'https://books.toscrape.com'
>>> response.status
200
```

Este shell es probablemente la herramienta que más vas a usar durante el desarrollo: te permite iterar rápido sobre los selectores sin tener que correr el spider completo cada vez.

También podés abrir el shell pasándole directamente una respuesta ya guardada, o inspeccionar visualmente la página con:

```python
>>> view(response)   # abre la página descargada en tu navegador
```

Esto es útil para confirmar que lo que Scrapy "ve" (el HTML crudo) coincide con lo que ves en el navegador — a veces no coincide, porque el contenido se generó con JavaScript (ver `07-manejo-avanzado.md`).

## 2.6. Correr un spider sin proyecto (`runspider`)

Si querés probar algo rápido sin crear un proyecto completo, podés escribir un spider en un solo archivo y correrlo directamente:

```python
# spider_suelto.py
import scrapy

class RapidoSpider(scrapy.Spider):
    name = "rapido"
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for libro in response.css("article.product_pod"):
            yield {"titulo": libro.css("h3 a::attr(title)").get()}
```

```bash
scrapy runspider spider_suelto.py -o salida.json
```

## Siguiente paso

Ahora que sabés crear y correr un spider, profundicemos en cómo extraer datos con selectores. Continuá con **[03-selectores.md](03-selectores.md)**.
