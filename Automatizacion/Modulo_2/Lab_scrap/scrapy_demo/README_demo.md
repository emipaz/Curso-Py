# Demo de Scrapy — guion para la clase

Contexto: la clase de hoy está centrada en BeautifulSoup básico, pero menciona
Scrapy por arriba (se retoma más adelante en el curso). Esta carpeta tiene
ejemplos chicos y **probados** para mostrar un poco más de Scrapy hoy, usando
dos sitios hechos para practicar scraping sin problemas legales/éticos:
[books.toscrape.com](https://books.toscrape.com) y
[quotes.toscrape.com](https://quotes.toscrape.com).

Todo el material de referencia más profundo ya está en
[`../../notas_Scrapy/`](../../notas_Scrapy/) (00 a 10). Esta carpeta es la
versión "para correr en vivo"; notas_Scrapy es para leer después con calma.

## Instalación (ya hecha en este repo)

```bash
uv add --system-certs scrapy
```

El `--system-certs` fue necesario en esta máquina porque `pip`/`requests`
tiraban `CERTIFICATE_VERIFY_FAILED` contra certifi (típico de proxy/antivirus
corporativo). Si en el aula pasa lo mismo al instalar con pip normal, probar
con `pip install --cacert <bundle>` o directamente `uv add --system-certs`.
Scrapy en sí (motor Twisted) no tuvo ese problema al correr.

## Orden sugerido (pensado para ~40-50 min dentro de las 2 horas)

### 1. Por qué Scrapy, en una frase (3 min)

BeautifulSoup + requests = **vos** armás el loop: pedís la página, parseás,
si hay que seguir un link pedís de nuevo a mano, si hay que pedir 50 páginas
las pedís una por una (secuencial). Scrapy = **un framework** que ya trae el
loop: motor asíncrono (pide varias páginas en paralelo), manejo de
reintentos/errores, exportación a JSON/CSV, respeto de `robots.txt`,
límites de velocidad (`AUTOTHROTTLE`). Pasás de "escribir el scraper" a
"declarar qué querés y cómo navegar".

Referencia para profundizar: `notas_Scrapy/01-introduccion.md`.

### 2. Shell interactivo — probar selectores en vivo (10 min)

Usar `00_shell_cheatsheet.md` como guía y tipear en vivo en la terminal:

```bash
uv run scrapy shell "https://books.toscrape.com"
```

Mensaje clave: los selectores CSS que ya conocen de BeautifulSoup
(`soup.select(...)`) tienen un equivalente casi directo en
`response.css(...)`. Lo nuevo es `::text` y `::attr(nombre)` para extraer
texto/atributos directamente en el selector, y `.get()` / `.getall()` en vez
de iterar manualmente.

### 3. El spider más chico posible, sin proyecto (5 min)

```bash
uv run scrapy runspider 01_mini_spider.py -o libros.json
```

Mostrar `01_mini_spider.py`: es literalmente una clase con `start_urls` y un
método `parse`. Remarcar:
- `yield` en vez de `return` (el spider es un generador).
- No hay loop manual: Scrapy llama a `parse` una vez por cada URL de
  `start_urls`, con la respuesta ya descargada.

### 4. Seguir enlaces (paginación) — la diferencia real con BS4 (10 min)

```bash
uv run scrapy runspider 02_spider_paginacion.py -a paginas=2 -o libros_detalle.jsonl
```

Mostrar `02_spider_paginacion.py`. Esto es lo que en BS4 requeriría un
`while` con `requests.get()` secuencial. Acá:
- `yield response.follow(url, callback=...)` encola una nueva request y
  sigue (no bloquea esperando).
- Scrapy maneja varias requests "al mismo tiempo" según
  `CONCURRENT_REQUESTS` (lo contrario a pedir página por página y esperar
  cada respuesta antes de pedir la siguiente).
- El parámetro `-a paginas=2` es para no barrer las 50 páginas del catálogo
  en vivo frente a la clase.

### 5. Un proyecto real: estructura, Items y Pipeline (10-15 min)

```bash
cd proyecto_demo
uv run scrapy crawl citas -o citas.jsonl
```

Mostrar la estructura de carpetas generada por `scrapy startproject` +
`scrapy genspider` (real, no inventada):

```
proyecto_demo/
├── scrapy.cfg
└── proyecto_demo/
    ├── items.py        <- CitaItem: la "forma" de los datos
    ├── pipelines.py    <- ValidarCitaPipeline + ContadorPipeline
    ├── settings.py     <- ITEM_PIPELINES, AUTOTHROTTLE_ENABLED
    └── spiders/
        └── citas.py    <- el spider en sí
```

Puntos para marcar:
- `items.py`: un `dataclass` que define los campos esperados (similar a
  construir un diccionario a mano en BS4, pero con nombre y tipo fijos).
- `pipelines.py`: código que se ejecuta **después** de que el spider extrae
  cada item — acá se valida (`ValidarCitaPipeline` descarta items sin texto o
  autor) y se cuenta (`ContadorPipeline`). En BS4 esa limpieza quedaría
  mezclada en el mismo loop de scraping.
- `settings.py`: `ROBOTSTXT_OBEY = True` y `AUTOTHROTTLE_ENABLED = True` ya
  vienen de fábrica — Scrapy "piensa" en scraping responsable por default,
  algo que en BS4 hay que acordarse de hacer a mano (poner un `time.sleep`,
  revisar `robots.txt` manualmente, etc.). Ver
  `notas_Scrapy/09-buenas-practicas-legales.md`.

### 6. Cierre (2 min)

- BS4 + requests: perfecto para scrapes chicos, una sola página, scripts
  rápidos (lo que ya vieron hoy).
- Scrapy: cuando hay que recorrer muchas páginas, seguir enlaces, manejar
  errores/reintentos, o exportar datos limpios de forma repetible.
- Más adelante en el curso se retoma en profundidad — esto fue un adelanto.
  Todo el detalle (middlewares, login, APIs, deploy) está en
  `notas_Scrapy/`.

## Archivos de esta carpeta

- `00_shell_cheatsheet.md` — comandos para el shell interactivo.
- `01_mini_spider.py` — spider de un archivo, sin proyecto.
- `02_spider_paginacion.py` — sigue enlaces y entra a páginas de detalle.
- `proyecto_demo/` — proyecto real (`startproject` + `genspider`) con items,
  pipeline y settings configurados.

Todos corridos y verificados antes de la clase (books.toscrape.com y
quotes.toscrape.com respondieron 200 y los datos extraídos son correctos).
