# 7. Manejo avanzado

## 7.1. Sitios con JavaScript: scrapy-playwright

Scrapy por sí solo **no ejecuta JavaScript** — solo descarga el HTML crudo que devuelve el servidor. Si un sitio carga contenido dinámicamente vía JS (SPAs con React, Vue, Angular, scroll infinito, etc.), hace falta renderizar la página con un navegador real. La integración recomendada hoy en día es **scrapy-playwright**.

### Instalación

```bash
pip install scrapy-playwright
playwright install   # descarga los binarios de los navegadores
```

### Configuración

```python
# settings.py
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
```

### Uso en el spider

```python
import scrapy

class SpaSpider(scrapy.Spider):
    name = "spa"

    def start_requests(self):
        yield scrapy.Request(
            "https://ejemplo-con-js.com",
            meta={"playwright": True},
            callback=self.parse,
        )

    def parse(self, response):
        # response.text ya contiene el HTML renderizado, después de ejecutar JS
        for item in response.css("div.producto"):
            yield {"titulo": item.css("h2::text").get()}
```

### Esperar a que aparezca un elemento específico

A veces el contenido tarda en cargar incluso con JS ejecutado. Se puede esperar explícitamente:

```python
yield scrapy.Request(
    url,
    meta={
        "playwright": True,
        "playwright_page_methods": [
            {"method": "wait_for_selector", "args": ["div.producto"]},
        ],
    },
    callback=self.parse,
)
```

### Interactuar con la página (clicks, scroll)

```python
meta={
    "playwright": True,
    "playwright_page_methods": [
        {"method": "click", "args": ["button.cargar-mas"]},
        {"method": "wait_for_timeout", "args": [1000]},
    ],
}
```

**Nota de rendimiento:** renderizar JS con un navegador real es mucho más lento y consume más recursos que descargar HTML plano. Conviene reservarlo solo para las páginas que realmente lo necesitan, y usar requests normales de Scrapy para el resto.

### Alternativa: scrapy-splash

`scrapy-splash` usa un servicio separado (Splash, corrido normalmente en Docker) especializado en renderizar JS de forma más liviana que un navegador completo. Es una alternativa más antigua pero todavía usada en algunos proyectos.

```bash
docker run -p 8050:8050 scrapinghub/splash
```

```python
# settings.py
SPLASH_URL = "http://localhost:8050"
DOWNLOADER_MIDDLEWARES = {
    "scrapy_splash.SplashCookiesMiddleware": 723,
    "scrapy_splash.SplashMiddleware": 725,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
}
SPIDER_MIDDLEWARES = {
    "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
}
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"
```

## 7.2. Rate limiting y AutoThrottle

Para no sobrecargar el sitio (y evitar bloqueos), Scrapy ofrece varias configuraciones:

```python
# settings.py

# Delay fijo entre requests al mismo dominio
DOWNLOAD_DELAY = 1  # 1 segundo

# Cantidad de requests concurrentes
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# AutoThrottle: ajusta el delay automáticamente según la latencia del sitio
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
AUTOTHROTTLE_DEBUG = True   # muestra en el log los delays calculados
```

`AutoThrottle` es especialmente recomendable: en vez de un delay fijo, mide el tiempo de respuesta del servidor y ajusta la velocidad dinámicamente — más rápido cuando el sitio responde bien, más lento si empieza a tardar (señal de que se está sobrecargando).

## 7.3. Manejo de errores

### Callback de errores (`errback`)

Para manejar excepciones específicas de una request (timeout, DNS no resuelto, conexión rechazada), se puede definir un `errback`:

```python
import scrapy
from twisted.internet.error import TimeoutError, DNSLookupError

class MiSpider(scrapy.Spider):
    name = "con_errores"

    def start_requests(self):
        yield scrapy.Request(
            "https://sitio-puede-fallar.com",
            callback=self.parse,
            errback=self.manejar_error,
        )

    def parse(self, response):
        yield {"titulo": response.css("h1::text").get()}

    def manejar_error(self, failure):
        if failure.check(TimeoutError):
            self.logger.error(f"Timeout en {failure.request.url}")
        elif failure.check(DNSLookupError):
            self.logger.error(f"DNS no resuelto: {failure.request.url}")
        else:
            self.logger.error(f"Error no manejado: {failure.value}")
```

### Manejar códigos de estado HTTP no exitosos

Por defecto, Scrapy ignora responses con códigos de error (4xx, 5xx) — ni siquiera llegan al callback `parse`. Para procesarlas explícitamente:

```python
class MiSpider(scrapy.Spider):
    name = "con_404"
    handle_httpstatus_list = [404, 403]

    def parse(self, response):
        if response.status == 404:
            self.logger.warning(f"Página no encontrada: {response.url}")
            return
        # procesamiento normal
```

## 7.4. Señales (signals): reaccionar a eventos del ciclo de vida

Scrapy emite señales en distintos momentos (inicio/fin del spider, item procesado, request programada, etc.), a las que te podés conectar para ejecutar lógica personalizada.

```python
# spider
from scrapy import signals

class MiSpider(scrapy.Spider):
    name = "con_señales"

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_cerrado, signal=signals.spider_closed)
        return spider

    def spider_cerrado(self, spider, reason):
        self.logger.info(f"Spider cerrado. Razón: {reason}")
        self.logger.info(f"Total items: {self.crawler.stats.get_value('item_scraped_count')}")
```

Señales comunes: `spider_opened`, `spider_closed`, `item_scraped`, `item_dropped`, `request_scheduled`, `response_received`.

## 7.5. Estadísticas del crawl

Scrapy acumula estadísticas automáticamente durante la ejecución (requests hechas, items extraídos, errores, tiempo total). Se pueden consultar en cualquier momento:

```python
def spider_cerrado(self, spider, reason):
    stats = self.crawler.stats.get_stats()
    print(stats)
```

Al final de cada `scrapy crawl`, esta información se imprime automáticamente en el log bajo `Dumping Scrapy stats`.

## 7.6. Simular distintos dispositivos / resoluciones (con Playwright)

```python
meta={
    "playwright": True,
    "playwright_context_kwargs": {
        "viewport": {"width": 375, "height": 812},
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)",
    },
}
```

## Siguiente paso

Ahora que conocés las herramientas para casos difíciles, veamos cómo configurar correctamente el proyecto para producción. Continuá con **[08-settings-y-despliegue.md](08-settings-y-despliegue.md)**.
