# Guía completa de Scrapy

Esta guía está dividida en varios documentos para facilitar la consulta:

1. **[01-introduccion.md](01-introduccion.md)** — Qué es Scrapy, arquitectura interna, instalación y cuándo conviene usarlo (vs. requests+BeautifulSoup, Playwright, etc.).
2. **[02-primeros-pasos.md](02-primeros-pasos.md)** — Crear un proyecto, estructura de carpetas, tu primer spider, ejecutarlo y guardar resultados.
3. **[03-selectores.md](03-selectores.md)** — CSS y XPath para extraer datos: sintaxis, ejemplos, `Selector`, `response.css()`, `response.xpath()`.
4. **[04-items-y-pipelines.md](04-items-y-pipelines.md)** — Definir `Item`/`dataclass`, `ItemLoader`, limpiar y validar datos, pipelines (guardar en DB, filtrar duplicados, exportar).
5. **[05-requests-avanzado.md](05-requests-avanzado.md)** — Seguir enlaces, paginación, formularios (`FormRequest`), APIs JSON, `meta`, `cb_kwargs`, prioridades, callbacks encadenados.
6. **[06-middlewares.md](06-middlewares.md)** — Downloader middlewares y spider middlewares: user-agents, proxies, rotación, reintentos, cookies, headers.
7. **[07-manejo-avanzado.md](07-manejo-avanzado.md)** — JavaScript (Splash/Playwright), autenticación, rate limiting, `AutoThrottle`, manejo de errores, señales (`signals`).
8. **[08-settings-y-despliegue.md](08-settings-y-despliegue.md)** — `settings.py` explicado, buenas prácticas de configuración, Scrapyd, Scrapy Cloud, cron.
9. **[09-buenas-practicas-legales.md](09-buenas-practicas-legales.md)** — `robots.txt`, límites éticos y legales, buenas prácticas de scraping responsable, errores comunes.
10. **[10-ejemplos-practicos.md](10-ejemplos-practicos.md)** — Casos reales: scraping de un catálogo de productos, scraping de noticias con paginación, spider con login, exportar a base de datos.

## Resumen rápido (TL;DR)

```bash
# Instalación
pip install scrapy

# Crear un proyecto
scrapy startproject miproyecto
cd miproyecto

# Generar un spider
scrapy genspider ejemplo ejemplo.com

# Correrlo y guardar resultados
scrapy crawl ejemplo -o resultados.json
```

```python
# spiders/ejemplo.py
import scrapy

class EjemploSpider(scrapy.Spider):
    name = "ejemplo"
    start_urls = ["https://ejemplo.com"]

    def parse(self, response):
        for producto in response.css("div.producto"):
            yield {
                "titulo": producto.css("h2::text").get(),
                "precio": producto.css("span.precio::text").get(),
            }
```

Si es tu primera vez con Scrapy, empezá por **01-introduccion.md**.
