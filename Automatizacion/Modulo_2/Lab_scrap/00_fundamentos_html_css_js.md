# HTML, CSS y JS — lo mínimo para poder scrapear

Antes de tocar BeautifulSoup o Scrapy hace falta entender QUÉ es lo que
estamos descargando y parseando. Esto es la base conceptual de toda la
clase: todo selector que vamos a escribir (`soup.select(...)`,
`response.css(...)`) apunta a algo definido acá.

## 1. HTML: la estructura (el "qué hay")

HTML es texto plano con **etiquetas** (`<algo>...</algo>`) que forman un
árbol anidado — cada etiqueta puede contener otras etiquetas adentro.

```html
<article class="product_pod">
  <h3><a href="libro1.html" title="A Light in the Attic">A Light...</a></h3>
  <p class="price_color">£51.77</p>
  <p class="instock availability">
    <i class="icon-ok"></i> In stock
  </p>
</article>
```

Vocabulario que vamos a usar todo el tiempo:

- **Etiqueta / tag**: `article`, `h3`, `a`, `p`, `i`. Define el tipo de
  elemento.
- **Atributo**: `class="price_color"`, `href="libro1.html"`. Pares
  `nombre="valor"` adentro de la etiqueta de apertura. `class` e `id` son
  los que más vamos a usar para "apuntar" a un elemento.
- **Anidamiento / árbol**: `<article>` es el padre de `<h3>`, `<p>`, etc.
  Cuando scrapeamos, navegamos este árbol: "dentro de cada `article`, buscá
  el `h3` y después el `a` que está adentro".
- **Texto del nodo**: lo que queda ENTRE las etiquetas (`A Light...`,
  `In stock`). Es lo que casi siempre queremos extraer.

Para ver el HTML real de cualquier página: click derecho → "Ver código
fuente de la página" (Ctrl+U), o F12 → pestaña Elements para ver el árbol
ya interpretado por el navegador (ver sección 3, por qué a veces estos dos
no coinciden).

## 2. CSS: cómo "apuntar" a un elemento (el "dónde")

CSS normalmente sirve para darle estilo a esos elementos, pero sus
**selectores** son exactamente lo que usamos para encontrarlos al
scrapear. No necesitamos escribir CSS de estilos, solo saber leer
selectores.

| Selector             | Significa                                      | Ejemplo sobre el HTML de arriba        |
|-----------------------|------------------------------------------------|------------------------------------------|
| `article`             | todas las etiquetas `<article>`               | el libro completo                        |
| `.price_color`        | cualquier elemento con `class="price_color"`  | el `<p>` del precio                      |
| `#algo`                | el elemento con `id="algo"` (único en la página) | —                                     |
| `article p`            | un `<p>` que esté **adentro** de un `<article>` (en cualquier nivel) | precio y disponibilidad |
| `p.instock.availability` | un `<p>` que tenga AMBAS clases          | el `<p>` de disponibilidad               |
| `h3 a`                 | un `<a>` adentro de un `<h3>`                  | el link del título                       |
| `h3 a::attr(title)`    | el ATRIBUTO `title` de ese `<a>` (sintaxis de Scrapy/`parsel`, no CSS puro) | `"A Light in the Attic"` |
| `h3 a::text`           | el TEXTO de ese `<a>` (idem)                    | `"A Light..."`                           |

`BeautifulSoup` usa `soup.select("article p.price_color")` (selector CSS
tal cual) o `soup.find("p", class_="price_color")` (su propio método).
Scrapy usa `response.css("article p.price_color::text")` — el mismo
selector CSS, más el agregado `::text`/`::attr()` que no es CSS estándar
sino una extensión de la librería `parsel` que usa Scrapy por debajo.

## 3. JavaScript: por qué a veces el HTML "no tiene" lo que buscás

El HTML que llega del servidor es una foto fija. JavaScript puede modificar
esa foto DESPUÉS de que cargó, agregando, borrando o rellenando elementos
sin que el servidor vuelva a enviar una página nueva. Ejemplo mínimo:

```html
<div id="contenedor"></div>
<script>
  // esto corre en el navegador, DESPUÉS de que el HTML ya llegó
  document.getElementById("contenedor").innerHTML = "<p>Dato cargado por JS</p>";
</script>
```

Si pedís esta página con `requests.get(url).text` (o Scrapy, que hace lo
mismo por debajo), vas a recibir el `<div id="contenedor"></div>` **vacío**
— el `<p>` que generó el `<script>` no está, porque nadie ejecutó ese
JavaScript. El navegador sí lo ejecuta, por eso cuando mirás con F12 →
Elements SÍ lo ves (eso es el DOM ya renderizado, no el HTML crudo).

**Esto es la línea que separa las herramientas:**

- `requests` + `BeautifulSoup`, y Scrapy por default → solo ven el HTML
  crudo que manda el servidor. Si el dato está armado por JS, no lo ven.
- `Selenium` / `Playwright` (y Scrapy combinado con `scrapy-playwright`) →
  prenden un navegador real, ejecutan el JS, y ahí sí extraen del DOM ya
  completo.

**Cómo detectarlo en 10 segundos** antes de elegir herramienta: Ctrl+U
(código fuente, sin JS) vs F12 → Elements (DOM renderizado, con JS). Si el
dato aparece en el segundo pero no en el primero, hace falta un navegador
real.

## Siguiente paso

Con esto ya alcanza para leer selectores CSS/XPath en BS4 y Scrapy. Ahora
toca la parte que faltaba: cómo se combina esto con regex, que es lo que
venimos viendo en el módulo anterior → ver
[`01_regex_y_html.py`](01_regex_y_html.py) y
[`02_regex_combinado_con_scraping.py`](02_regex_combinado_con_scraping.py).
