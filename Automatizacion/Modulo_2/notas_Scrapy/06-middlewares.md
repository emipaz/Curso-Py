# 6. Middlewares

Los middlewares son "ganchos" que interceptan requests y responses en distintos puntos del flujo, permitiendo modificarlos, filtrarlos o reaccionar a errores. Hay dos tipos: **Downloader Middlewares** (entre el Engine y el Downloader) y **Spider Middlewares** (entre el Engine y los Spiders). En la práctica, los Downloader Middlewares son los que más se usan.

## 6.1. Rotar User-Agent

Muchos sitios bloquean o limitan requests que usan el user-agent por defecto de Scrapy. Un middleware simple:

```python
# middlewares.py
import random

class RotarUserAgentMiddleware:
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    ]

    def process_request(self, request, spider):
        request.headers["User-Agent"] = random.choice(self.USER_AGENTS)
```

```python
# settings.py
DOWNLOADER_MIDDLEWARES = {
    "miproyecto.middlewares.RotarUserAgentMiddleware": 400,
}
```

Para algo más robusto y mantenido, conviene usar la librería `scrapy-user-agents` en vez de mantener una lista propia:

```bash
pip install scrapy-user-agents
```

```python
# settings.py
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
}
```

## 6.2. Rotar proxies

```python
# middlewares.py
import random

class RotarProxyMiddleware:
    PROXIES = [
        "http://proxy1.ejemplo.com:8000",
        "http://proxy2.ejemplo.com:8000",
    ]

    def process_request(self, request, spider):
        request.meta["proxy"] = random.choice(self.PROXIES)
```

Para servicios de proxies comerciales (rotación automática, proxies residenciales, etc.) normalmente se usa el middleware que provee el propio servicio (por ejemplo, Zyte Smart Proxy Manager, Bright Data, o similares), en vez de mantener una lista manual — más confiable y con mejores tasas de éxito.

## 6.3. Middleware de reintentos personalizado

Scrapy ya trae un middleware de reintentos activado por defecto (`RetryMiddleware`), configurable así:

```python
# settings.py
RETRY_ENABLED = True
RETRY_TIMES = 3                        # cantidad de reintentos
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]
```

Si necesitás lógica de reintento personalizada (por ejemplo, reintentar también ante ciertos contenidos de la respuesta, no solo códigos HTTP), se puede extender:

```python
from scrapy.downloadermiddlewares.retry import RetryMiddleware

class ReintentoPersonalizado(RetryMiddleware):
    def process_response(self, request, response, spider):
        if "captcha" in response.text.lower():
            spider.logger.warning(f"Captcha detectado en {request.url}, reintentando...")
            return self._retry(request, "Captcha detectado", spider) or response
        return super().process_response(request, response, spider)
```

## 6.4. Manejo de cookies

Scrapy maneja cookies automáticamente entre requests dentro de la misma sesión (activado por defecto vía `CookiesMiddleware`). Para desactivarlo en requests puntuales (por ejemplo, para evitar que el sitio "recuerde" el estado entre requests paralelas):

```python
yield scrapy.Request(url, meta={"dont_merge_cookies": True})
```

Para pasar cookies manualmente:

```python
yield scrapy.Request(
    url,
    cookies={"session_id": "abc123"},
    callback=self.parse,
)
```

Para simular múltiples sesiones independientes en paralelo (por ejemplo, scrapear con distintas cuentas), se usa `cookiejar` en `meta`:

```python
yield scrapy.Request(url, meta={"cookiejar": "sesion_usuario_1"})
```

## 6.5. Middleware para headers personalizados

```python
class HeadersMiddleware:
    def process_request(self, request, spider):
        request.headers["Accept-Language"] = "es-AR,es;q=0.9"
        request.headers["Referer"] = "https://google.com"
```

## 6.6. Spider Middleware: filtrar o modificar items/requests generados

Los spider middlewares operan sobre lo que el spider genera (items y requests), no sobre requests/responses del downloader. Un ejemplo típico es filtrar automáticamente requests fuera de dominio (aunque esto ya lo hace `allowed_domains` por defecto vía `OffsiteMiddleware`).

```python
class FiltrarPorPalabraMiddleware:
    def process_spider_output(self, response, result, spider):
        for x in result:
            if isinstance(x, dict) and "spam" in x.get("titulo", "").lower():
                continue  # descarta este item
            yield x
```

```python
# settings.py
SPIDER_MIDDLEWARES = {
    "miproyecto.middlewares.FiltrarPorPalabraMiddleware": 500,
}
```

## 6.7. Orden de ejecución de middlewares

El número asociado a cada middleware en `settings.py` determina el orden: para requests salientes, se procesan de menor a mayor número (hacia el Downloader); para responses entrantes, en orden inverso (de mayor a menor, hacia el Spider). Esto importa cuando tenés varios middlewares que dependen unos de otros (por ejemplo, primero setear el proxy, después rotar el user-agent).

```python
DOWNLOADER_MIDDLEWARES = {
    "miproyecto.middlewares.RotarProxyMiddleware": 350,
    "miproyecto.middlewares.RotarUserAgentMiddleware": 400,
    "miproyecto.middlewares.ReintentoPersonalizado": 550,
}
```

## 6.8. Middlewares de terceros útiles

- **`scrapy-user-agents`**: rotación de user-agents realista basada en una base de datos actualizada.
- **`scrapy-fake-useragent`**: alternativa similar.
- **`scrapy-rotating-proxies`**: rotación y verificación de salud de una lista de proxies propia.
- **`scrapy-playwright`**: renderizado de JavaScript integrado como downloader handler (ver `07-manejo-avanzado.md`).
- **`scrapy-splash`**: alternativa para renderizar JS usando el servicio Splash.

## Siguiente paso

Para sitios con JavaScript, autenticación compleja, rate limiting fino y manejo de errores/señales, seguí con **[07-manejo-avanzado.md](07-manejo-avanzado.md)**.
