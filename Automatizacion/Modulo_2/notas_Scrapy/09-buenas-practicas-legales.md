# 9. Buenas prácticas legales y éticas

Este documento es informativo y no constituye asesoramiento legal — las leyes varían por país y por caso concreto. Si el scraping que planeás hacer tiene implicancias comerciales o legales importantes, conviene consultar con un profesional.

## 9.1. `robots.txt`: qué es y por qué importa

`robots.txt` es un archivo estándar (no legalmente vinculante por sí solo, pero ampliamente respetado como norma de buena práctica) que los sitios publican en la raíz de su dominio (ej. `https://ejemplo.com/robots.txt`) indicando qué rutas no deberían ser accedidas por bots automatizados.

```
User-agent: *
Disallow: /admin/
Disallow: /buscar
Crawl-delay: 2
```

Scrapy respeta este archivo automáticamente cuando `ROBOTSTXT_OBEY = True` está activado en `settings.py` (que es el valor por defecto en proyectos nuevos). **Se recomienda mantenerlo activado**, salvo que tengas una razón específica y justificada para desactivarlo (por ejemplo, sos dueño del sitio que estás scrapeando).

## 9.2. Términos de servicio (ToS)

Además de `robots.txt`, muchos sitios incluyen cláusulas en sus Términos de Servicio que prohíben explícitamente el scraping automatizado. A diferencia de `robots.txt` (que es una convención técnica), los ToS pueden tener **implicancias contractuales y legales reales**, especialmente si:

- El sitio requiere una cuenta/login para acceder (aceptaste los ToS al registrarte).
- Los datos scrapeados se usan con fines comerciales.
- El scraping impone una carga significativa sobre la infraestructura del sitio.

**Recomendación:** antes de scrapear un sitio a gran escala, revisá sus Términos de Servicio. Si tenés dudas sobre la legalidad de un proyecto específico, consultá a un abogado — esto no es un tema que se pueda resolver únicamente con buenas prácticas técnicas.

## 9.3. Datos personales y privacidad

Si el scraping involucra datos personales (nombres, emails, teléfonos, fotos de personas identificables), aplican regulaciones de protección de datos según la jurisdicción — por ejemplo **GDPR** en la Unión Europea, o leyes locales de protección de datos personales en otros países. Recolectar y almacenar datos personales sin base legal puede tener consecuencias legales serias, independientemente de que la información esté "públicamente visible" en un sitio web.

## 9.4. Buenas prácticas técnicas para un scraping responsable

Independientemente del marco legal, estas prácticas reducen el impacto sobre el sitio scrapeado y la probabilidad de ser bloqueado:

### Identificarte claramente

```python
USER_AGENT = "MiEmpresa Bot (+http://miempresa.com/bot-info) contacto@miempresa.com"
```

Un user-agent identificable permite que el administrador del sitio te contacte si hay un problema, en vez de simplemente bloquearte.

### Limitar la velocidad y concurrencia

```python
DOWNLOAD_DELAY = 2
CONCURRENT_REQUESTS_PER_DOMAIN = 4
AUTOTHROTTLE_ENABLED = True
```

Scrapear "lo más rápido posible" puede sobrecargar servidores pequeños (equivalente en efecto a un ataque de denegación de servicio, aunque no sea la intención).

### Scrapear solo lo necesario

- Evitar descargar recursos que no necesitás (imágenes pesadas, videos) si solo te interesa texto.
- Cachear localmente durante el desarrollo (`HTTPCACHE_ENABLED = True`) para no re-descargar innecesariamente.
- Evitar recorrer el sitio completo si solo necesitás una sección específica.

### Horarios de menor tráfico

Si el volumen de scraping es considerable, correr el crawl en horarios de bajo tráfico del sitio objetivo (de madrugada según su zona horaria, por ejemplo) reduce el impacto sobre usuarios reales.

### Preferir APIs oficiales cuando existen

Si el sitio ofrece una API pública oficial para acceder a los mismos datos, es preferible usarla en vez de scrapear el HTML: es más estable, generalmente está pensada para ese uso, y evita zonas grises legales.

## 9.5. Errores comunes (no legales, técnicos)

### No manejar la paginación correctamente (loops infinitos)

Sin una condición de corte clara, un spider mal escrito puede quedar recorriendo enlaces indefinidamente (por ejemplo, un calendario que siempre tiene un "mes siguiente"). Usá `DEPTH_LIMIT` o condiciones explícitas de corte.

### Ignorar cambios en la estructura del sitio

Los selectores CSS/XPath dependen de la estructura HTML actual del sitio, que puede cambiar sin aviso. Es recomendable:

- Agregar validaciones en el pipeline (`DropItem` si faltan campos críticos).
- Loggear advertencias cuando un selector no encuentra nada, para detectar rupturas rápido.
- Monitorear la tasa de items extraídos por corrida; una caída abrupta suele indicar que el sitio cambió su HTML.

### No manejar bloqueos o CAPTCHAs

Si empezás a recibir muchos 403/429 o páginas de CAPTCHA, seguir insistiendo agresivamente empeora la situación (y puede llevar a un bloqueo permanente de IP). Es mejor:

- Bajar la concurrencia y aumentar el delay.
- Rotar proxies/user-agents de forma más conservadora.
- En algunos casos, aceptar que ese sitio requiere una integración distinta (API oficial, servicio de terceros especializado en anti-bot bypass legítimo, o contacto directo con el sitio).

### Guardar datos sin control de duplicados

En corridas recurrentes (ej. diarias), sin un pipeline de deduplicación los datos se acumulan con muchísima redundancia. Ver el pipeline de duplicados en `04-items-y-pipelines.md`.

## 9.6. Checklist antes de scrapear un sitio nuevo

1. ¿Revisé `robots.txt` y los Términos de Servicio del sitio?
2. ¿El sitio ofrece una API pública que cubra mi necesidad, evitando el scraping del HTML?
3. ¿Estoy recolectando datos personales? Si es así, ¿tengo base legal para hacerlo?
4. ¿Configuré `AUTOTHROTTLE_ENABLED` y un `DOWNLOAD_DELAY` razonable?
5. ¿Mi `USER_AGENT` es identificable y no intenta suplantar a un navegador para evadir bloqueos deliberadamente?
6. ¿Tengo un plan para lo que voy a hacer con los datos (uso interno, reventa, análisis, etc.), y ese uso es compatible con lo permitido por el sitio?

## Siguiente paso

Con todo esto en mente, veamos ejemplos completos y realistas. Continuá con **[10-ejemplos-practicos.md](10-ejemplos-practicos.md)**.
