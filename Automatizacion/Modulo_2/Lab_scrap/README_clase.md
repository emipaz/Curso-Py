# Guion de la clase de hoy — Web Scraping

Orden pensado para las 2 horas, con lo que prometiste sumar (fundamentos de
HTML/CSS/JS, y scrapear combinando regex) antes de llegar a BS4 (el
contenido "oficial" de hoy) y, si llega el tiempo, un adelanto de Scrapy.

## 0. Por qué este orden

El curso ya vio regex a fondo (el módulo anterior). Antes de BS4 hace falta
que entiendan QUÉ es el HTML/CSS/JS que van a parsear, y después conectar
con lo que ya saben de regex — mostrando dónde regex ayuda y dónde se rompe
— para que BS4 se sienta como "la herramienta correcta para esto" y no como
algo que cae de la nada.

## 1. Fundamentos HTML / CSS / JS (~15 min)

Archivo: [`00_fundamentos_html_css_js.md`](00_fundamentos_html_css_js.md)

- HTML: etiquetas, atributos, anidamiento/árbol, texto del nodo.
- CSS: selectores (`tag`, `.clase`, `#id`, `tag tag`, `.clase.clase`) y las
  extensiones `::text` / `::attr()` que usa Scrapy (no son CSS estándar).
- JS: por qué el HTML crudo a veces no tiene el dato (se arma con JS
  después) — Ctrl+U vs F12 Elements como truco rápido para detectarlo.
  Esto conecta con la pregunta que surgió sobre Selenium/Playwright vs
  BS4/Scrapy.

## 2. Por qué regex solo no alcanza para HTML (~10 min)

Archivo: [`01_regex_y_html.py`](01_regex_y_html.py) — corre sin internet.

```bash
uv run python Lab_scrap/01_regex_y_html.py
```

Muestra en vivo el caso clásico: greedy (`.*`) vs perezoso (`.*?`) con dos
`<a>` en la misma línea — con greedy se "pierde" el primer título. Y aunque
perezoso arregla eso, un cambio en el ORDEN de los atributos ya rompe el
patrón. Mensaje: regex no entiende árbol ni orden de atributos, un parser
(BS4/Scrapy) sí.

## 3. El combo que SI funciona: parser + regex (~10 min)

Archivo: [`02_regex_combinado_con_scraping.py`](02_regex_combinado_con_scraping.py)
— pide `books.toscrape.com` de verdad.

```bash
uv run python Lab_scrap/02_regex_combinado_con_scraping.py
```

BS4 aísla el nodo correcto (`article.product_pod`, `p.price_color`, etc.);
regex limpia/extrae DEL TEXTO YA AISLADO: separar el precio numérico del
símbolo de moneda, mapear `"star-rating Three"` a `3`, sacar el ID numérico
de la URL del libro. Esto es "cumplir la promesa" de scrapear con regex, de
forma que además es robusta.

**Bonus si da el tiempo** — datos que ya vienen en el HTML aunque "parezcan"
puestos por JS: [`03_regex_json_embebido.py`](03_regex_json_embebido.py)
(sin internet, HTML de ejemplo con un `<script>` que trae un JSON). Muestra
que no todo lo que menciona JS necesita Selenium/Playwright — a veces el
dato ya está en el código fuente y un regex + `json.loads()` alcanza.

## 3.5. Bonus — cuando el bloqueo no es por JS, sino por "fingerprint" (~5 min)

Archivo: [`04_primp_impersonar_navegador.py`](04_primp_impersonar_navegador.py)

Conecta con la pregunta de la clase pasada sobre páginas dinámicas: hay un
TERCER motivo (además de "falta JS" y "el dato ya está en un `<script>`")
por el que un scrape puede fallar — el servidor bloquea la conexión porque
detecta que no es un navegador real (el header `User-Agent` dice
`python-requests/x.y`, y el *fingerprint* TLS del handshake tampoco
coincide con el de un browser). `primp` es un cliente HTTP (ligero, sin
navegador) que imita ese fingerprint. La demo pega contra
`tls.peet.ws/api/all` (servicio público para auto-diagnóstico, no estamos
esquivando la protección de nadie) y compara el JA3 hash y el User-Agent de
`requests` vs `primp`.

```bash
uv add --system-certs primp
uv run python Lab_scrap/04_primp_impersonar_navegador.py
```

## 4. BeautifulSoup — el contenido central de hoy

Esto ya está armado en el curso:
- Teoría: [`22_intro_bs4.md`](../22_intro_bs4.md),
  [`29_Web_Scraping_guia.md`](../29_Web_Scraping_guia.md).
- Notebook: [`Modulo_2_Web_Scraping.ipynb`](../Modulo_2_Web_Scraping.ipynb).
- Lab práctico: [`main.py`](main.py) + [`baseball_stats.html`](baseball_stats.html)
  (ejercicio para completar en vivo con el grupo).

Con los puntos 1-3 ya hechos, acá podés conectar directo: "esto que vieron
en regex, ya lo usamos arriba junto con BS4; ahora vamos a usar BS4 solo,
para que entiendan bien su sintaxis propia (`find`, `find_all`,
`select`)".

## 5. Bonus — adelanto de Scrapy (si queda tiempo)

Carpeta [`scrapy_demo/`](scrapy_demo/) con su propio guion en
[`scrapy_demo/README_demo.md`](scrapy_demo/README_demo.md): shell
interactivo, spider mínimo, paginación con `response.follow`, y un proyecto
real con items/pipelines. Todo ya probado contra books.toscrape.com y
quotes.toscrape.com.

## Instalación necesaria para esta máquina

```bash
uv add --system-certs scrapy truststore primp
```

`truststore` se usa en `02_regex_combinado_con_scraping.py` únicamente por
el certificado TLS corporativo de esta máquina (ver comentario al inicio
del archivo) — en el aula, si no da error de SSL, se puede sacar esa parte
del código sin que cambie nada más.
