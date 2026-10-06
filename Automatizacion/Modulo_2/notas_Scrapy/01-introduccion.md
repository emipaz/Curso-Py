# 1. Introducción a Scrapy

## ¿Qué es Scrapy?

**Scrapy** es un framework de Python para hacer **web scraping** (extracción de datos de sitios web) y **web crawling** (recorrer sitios siguiendo enlaces) de forma estructurada, rápida y escalable. A diferencia de armar un scraper "a mano" con `requests` + `BeautifulSoup`, Scrapy provee toda la infraestructura necesaria: manejo de requests concurrentes, cola de URLs, reintentos, exportación de datos, middlewares para proxies/cookies/user-agents, y mucho más — todo integrado.

Fue creado originalmente por la empresa Scrapinghub (hoy Zyte) y es el framework de scraping más usado y maduro del ecosistema Python.

## Arquitectura interna (a alto nivel)

Scrapy funciona con un motor **asíncrono** basado en Twisted (y opcionalmente asyncio desde versiones recientes). Los componentes principales son:

- **Engine (motor)**: coordina el flujo de datos entre todos los componentes.
- **Scheduler (planificador)**: mantiene la cola de requests pendientes.
- **Downloader**: descarga las páginas web (hace las requests HTTP reales).
- **Spiders**: tu código, donde defines qué URLs visitar y cómo extraer datos de cada respuesta.
- **Item Pipeline**: procesa los datos extraídos (limpieza, validación, guardado en base de datos, etc.).
- **Downloader Middlewares**: se ejecutan entre el Engine y el Downloader — ideales para modificar requests/responses (proxies, headers, cookies, reintentos).
- **Spider Middlewares**: se ejecutan entre el Engine y los Spiders — para procesar la entrada/salida de los spiders.

El flujo básico es:

```
Spider genera Request → Scheduler la encola → Downloader la descarga
   → Response vuelve al Spider → Spider extrae Items y/o nuevas Requests
   → Items van al Item Pipeline → nuevas Requests vuelven al Scheduler
```

Gracias a este diseño asíncrono, Scrapy puede hacer **muchas requests en paralelo** sin necesidad de threads ni multiprocessing manual — algo mucho más eficiente que un loop secuencial con `requests.get()`.

## ¿Por qué usar Scrapy en vez de requests + BeautifulSoup?

| Característica | requests + BeautifulSoup | Scrapy |
|---|---|---|
| Concurrencia | Manual (threading/asyncio) | Integrada, configurable con una línea |
| Seguir enlaces / crawling | Manual | Integrado (`response.follow`, reglas de `CrawlSpider`) |
| Exportar a JSON/CSV/XML | Manual | Integrado (`-o archivo.json`) |
| Reintentos automáticos | Manual | Integrado (middleware de reintentos) |
| Manejo de cookies/sesión | Manual | Integrado |
| Rotación de proxies/user-agents | Manual | Vía middlewares (propios o de terceros) |
| Rate limiting / AutoThrottle | Manual | Integrado |
| Curva de aprendizaje | Baja | Media (hay que entender la arquitectura) |
| Ideal para... | Scripts puntuales, una sola página | Proyectos de crawling grande, recurrentes, con muchas páginas |

**Regla general:** si necesitás extraer datos de una sola página o de un puñado de URLs conocidas, `requests` + `BeautifulSoup` alcanza y es más simple. Si necesitás **recorrer** un sitio completo, manejar miles de páginas, paginación, reintentos, exportación y velocidad, Scrapy es la herramienta correcta.

## ¿Cuándo Scrapy NO es la mejor opción?

- **Sitios que dependen fuertemente de JavaScript** (contenido renderizado del lado del cliente, SPAs con React/Vue): Scrapy no ejecuta JavaScript por sí solo. Se puede combinar con `scrapy-playwright` o `scrapy-splash` (ver `07-manejo-avanzado.md`), pero si el sitio es 100% JS, a veces es más simple usar directamente **Playwright** o **Selenium**.
- **Un scraping único y simple de una sola página**: el overhead de crear un proyecto Scrapy completo puede no valer la pena; un script con `requests` alcanza.
- **Cuando necesitás control fino de un navegador real** (clicks, scroll infinito, formularios complejos con JS): herramientas de automatización de navegador son más apropiadas como motor principal.

## Instalación

```bash
pip install scrapy
```

Scrapy tiene algunas dependencias que a veces requieren compilación (como `lxml`, `cryptography`, `Twisted`). En Linux normalmente instala sin problemas; en Windows a veces conviene usar `conda` o wheels precompilados si hay errores de compilación.

Verificar instalación:

```bash
scrapy version
```

## Siguiente paso

Continuá con **[02-primeros-pasos.md](02-primeros-pasos.md)** para crear tu primer proyecto y spider.
