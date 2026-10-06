# 8. Settings y despliegue

## 8.1. Settings más importantes explicados

```python
# settings.py

BOT_NAME = "miproyecto"

SPIDER_MODULES = ["miproyecto.spiders"]
NEWSPIDER_MODULE = "miproyecto.spiders"

# --- Identificación ---
USER_AGENT = "miproyecto (+http://www.miempresa.com)"

# --- Respeto al sitio ---
ROBOTSTXT_OBEY = True          # respeta robots.txt (ver 09-buenas-practicas-legales.md)
DOWNLOAD_DELAY = 1              # segundos de espera entre requests al mismo dominio

# --- Concurrencia ---
CONCURRENT_REQUESTS = 16                    # requests concurrentes totales
CONCURRENT_REQUESTS_PER_DOMAIN = 8          # requests concurrentes por dominio
CONCURRENT_REQUESTS_PER_IP = 0              # 0 = usar el límite por dominio en su lugar

# --- AutoThrottle (recomendado en vez de DOWNLOAD_DELAY fijo) ---
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10

# --- Reintentos ---
RETRY_ENABLED = True
RETRY_TIMES = 3

# --- Timeouts ---
DOWNLOAD_TIMEOUT = 15

# --- Caché HTTP (útil en desarrollo, evita re-descargar en cada corrida) ---
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0    # 0 = nunca expira
HTTPCACHE_DIR = "httpcache"

# --- Exportación ---
FEED_EXPORT_ENCODING = "utf-8"   # evita problemas con tildes/ñ en JSON/CSV

# --- Logs ---
LOG_LEVEL = "INFO"                # DEBUG, INFO, WARNING, ERROR
```

### `ROBOTSTXT_OBEY`

Cuando está en `True` (default desde hace varias versiones), Scrapy consulta automáticamente el archivo `robots.txt` del sitio y **descarta** requests a rutas que el sitio marca como no permitidas para bots. Ver la discusión ética/legal completa en `09-buenas-practicas-legales.md`.

### `HTTPCACHE_ENABLED`

Extremadamente útil durante el **desarrollo**: si activás la caché, Scrapy guarda cada response en disco y, si volvés a pedir la misma URL, la sirve desde el caché local en vez de volver a golpear el sitio real. Esto acelera muchísimo el ciclo de prueba-error mientras escribís los selectores, y evita generar carga innecesaria al sitio mientras estás iterando.

**Importante:** desactivar `HTTPCACHE_ENABLED` (o borrar la carpeta de caché) antes de una corrida real en producción, para no trabajar con datos desactualizados.

## 8.2. Settings por spider

Se pueden sobreescribir settings para un spider específico sin afectar al resto del proyecto:

```python
class MiSpider(scrapy.Spider):
    name = "mi_spider"

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 2,
        "ITEM_PIPELINES": {
            "miproyecto.pipelines.SQLitePipeline": 300,
        },
    }
```

Esto es útil cuando distintos spiders scrapean sitios con distintas políticas de tolerancia (uno puede aguantar mayor concurrencia, otro requiere ser mucho más conservador).

## 8.3. Variables de entorno y configuración sensible

Para credenciales (API keys, proxies con auth, credenciales de base de datos), no conviene hardcodearlas en `settings.py`. Se recomienda usar variables de entorno:

```python
# settings.py
import os

DATABASE_URL = os.environ.get("DATABASE_URL")
PROXY_API_KEY = os.environ.get("PROXY_API_KEY")
```

```bash
export DATABASE_URL="postgresql://usuario:pass@host/db"
scrapy crawl mi_spider
```

O usando un archivo `.env` con la librería `python-dotenv`.

## 8.4. Ejecutar spiders desde código Python (no solo CLI)

Para integrar Scrapy dentro de otro programa (por ejemplo, un script que corre varios spiders programáticamente, o un servicio que dispara crawls bajo demanda), se usa `CrawlerProcess`:

```python
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from miproyecto.spiders.libros import LibrosSpider

process = CrawlerProcess(get_project_settings())
process.crawl(LibrosSpider)
process.start()   # bloquea hasta que el crawl termina
```

### Correr varios spiders en la misma corrida

```python
process = CrawlerProcess(get_project_settings())
process.crawl(LibrosSpider)
process.crawl(OtroSpider)
process.start()
```

**Nota:** `CrawlerProcess` solo puede usarse **una vez por proceso** de Python (Twisted no permite reiniciar el reactor). Si necesitás correr crawls repetidamente dentro de una aplicación de larga duración, se usa `CrawlerRunner` en combinación con el manejo manual del reactor de Twisted, o se lanza cada crawl como un subproceso separado.

## 8.5. Programar ejecuciones periódicas

Scrapy no incluye un scheduler propio. Las formas más comunes de programar ejecuciones periódicas:

### Cron (Linux/macOS)

```bash
# Ejecutar todos los días a las 3am
0 3 * * * cd /ruta/miproyecto && /ruta/venv/bin/scrapy crawl libros -o "resultados_$(date +\%Y\%m\%d).json"
```

### Scrapyd

**Scrapyd** es un servicio (creado por el mismo equipo de Scrapy) para desplegar y correr spiders vía una API HTTP, con soporte para programar, versionar y monitorear ejecuciones.

```bash
pip install scrapyd
scrapyd   # levanta el servicio, por defecto en localhost:6800
```

Deploy del proyecto:

```bash
pip install scrapyd-client
scrapyd-deploy
```

Disparar un crawl vía API:

```bash
curl http://localhost:6800/schedule.json -d project=miproyecto -d spider=libros
```

### Scrapy Cloud (Zyte)

**Scrapy Cloud** es el servicio administrado de la empresa Zyte (creadores de Scrapy) para desplegar, programar y monitorear spiders sin manejar tu propia infraestructura. Incluye dashboard, logs, alertas, y manejo de proxies integrado. Es la opción más simple si no querés mantener servidores propios.

## 8.6. Buenas prácticas de configuración para producción

```python
# settings.py — configuración recomendada para producción
ROBOTSTXT_OBEY = True
AUTOTHROTTLE_ENABLED = True
RETRY_ENABLED = True
RETRY_TIMES = 3
HTTPCACHE_ENABLED = False        # desactivado en producción (solo para desarrollo)
LOG_LEVEL = "INFO"
FEED_EXPORT_ENCODING = "utf-8"

# Alertar/loggear en caso de que el spider termine sin items (posible bloqueo)
CLOSESPIDER_ERRORCOUNT = 50      # cierra el spider si supera N errores
```

`CLOSESPIDER_ERRORCOUNT`, `CLOSESPIDER_ITEMCOUNT`, `CLOSESPIDER_PAGECOUNT` y `CLOSESPIDER_TIMEOUT` son útiles como "circuit breakers": cierran el spider automáticamente si algo empieza a salir mal (por ejemplo, si de golpe empiezan a fallar todas las requests, probablemente el sitio te esté bloqueando).

## Siguiente paso

Antes de scrapear cualquier sitio real, es importante conocer los límites éticos y legales. Continuá con **[09-buenas-practicas-legales.md](09-buenas-practicas-legales.md)**.
