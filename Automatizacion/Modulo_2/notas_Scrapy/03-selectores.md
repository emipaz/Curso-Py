# 3. Selectores: CSS y XPath

Scrapy usa la librería `parsel` internamente para seleccionar datos del HTML, soportando tanto **selectores CSS** como **XPath**. Podés usar el que prefieras (o combinarlos).

## 3.1. Selectores CSS

### Sintaxis básica

```python
response.css("div.producto")          # por clase
response.css("#id-especifico")         # por id
response.css("a")                       # por etiqueta
response.css("div.producto > h2")       # hijo directo
response.css("div.producto h2")         # descendiente
response.css("div.producto:nth-child(2)")  # pseudo-selector
```

### Extraer texto y atributos

Con selectores CSS, se usan pseudo-elementos especiales de Scrapy (no son CSS estándar, son una extensión de `parsel`):

```python
response.css("h1::text").get()              # texto del elemento
response.css("a::attr(href)").get()          # valor de un atributo
response.css("img::attr(src)").getall()      # todos los atributos src
```

### `.get()` vs `.getall()`

```python
response.css("h3 a::attr(title)").get()      # primer resultado (string) o None si no hay matches
response.css("h3 a::attr(title)").getall()   # lista con TODOS los resultados
```

`.get()` acepta un valor por defecto si no hay match, para evitar `None`:

```python
response.css("span.precio::text").get(default="Sin precio")
```

### Encadenar selectores

Se puede seguir refinando la búsqueda dentro de un selector ya obtenido:

```python
for producto in response.css("div.producto"):
    titulo = producto.css("h2::text").get()
    precio = producto.css("span.precio::text").get()
```

Esto es clave: `producto.css(...)` busca **dentro** de ese elemento específico, no en toda la página — así evitás mezclar datos de distintos productos.

## 3.2. Selectores XPath

XPath es más poderoso que CSS para casos complejos (navegar hacia arriba en el árbol, condiciones basadas en texto, lógica más avanzada).

### Sintaxis básica

```python
response.xpath("//div[@class='producto']")            # por clase exacta
response.xpath("//div[contains(@class, 'producto')]")  # clase que contiene un valor
response.xpath("//a/@href")                              # atributo href
response.xpath("//h1/text()")                             # texto
response.xpath("//div[@id='main']//p")                    # descendientes
```

### Extraer

```python
response.xpath("//h1/text()").get()
response.xpath("//a/@href").getall()
```

### Casos donde XPath es más potente que CSS

**Buscar por texto contenido:**

```python
response.xpath("//button[contains(text(), 'Comprar')]")
```

**Navegar hacia el padre** (CSS no puede hacer esto):

```python
response.xpath("//span[@class='precio']/parent::div")
```

**Seleccionar por posición con lógica compleja:**

```python
response.xpath("//tr[position() > 1]")   # todas las filas excepto la primera (ej: saltar encabezado de tabla)
```

**Combinar múltiples condiciones:**

```python
response.xpath("//div[@class='producto' and @data-disponible='true']")
```

## 3.3. Tabla comparativa CSS vs XPath

| Necesidad | CSS | XPath |
|---|---|---|
| Seleccionar por clase | ✅ Simple | ✅ Más verboso |
| Seleccionar por texto contenido | ❌ No soportado | ✅ `contains(text(), '...')` |
| Navegar al elemento padre | ❌ No soportado | ✅ `parent::` o `..` |
| Selección por posición | Parcial (`:nth-child`) | ✅ `position()` |
| Legibilidad para casos simples | ✅ Más legible | Más verboso |

**Recomendación práctica:** usá CSS para casos simples (la mayoría) y recurrí a XPath cuando necesites algo que CSS no puede expresar (navegar al padre, filtrar por texto, condiciones complejas).

## 3.4. Selectores y expresiones regulares

Se puede combinar con `re()` para extraer solo una parte del texto usando regex:

```python
response.css("span.precio::text").re(r"[\d.]+")        # extrae solo números
response.css("span.precio::text").re_first(r"[\d.]+")   # solo el primer match
```

Esto es útil cuando el texto tiene formato mixto, por ejemplo `"Precio: $19.99 USD"` y solo querés `19.99`.

## 3.5. Selectores anidados y `Selector` standalone

Si tenés un string de HTML fuera de una respuesta de Scrapy (por ejemplo, un fragmento guardado en base de datos), podés crear un `Selector` directamente:

```python
from scrapy import Selector

html = "<div><h1>Título</h1></div>"
sel = Selector(text=html)
sel.css("h1::text").get()
```

## 3.6. Limpiar espacios y saltos de línea

Es muy común que el texto extraído venga con espacios extra o saltos de línea. Un patrón habitual:

```python
titulo = response.css("h1::text").get()
titulo = titulo.strip() if titulo else None
```

O usando `join()` cuando el texto está repartido en varios nodos:

```python
descripcion = " ".join(response.css("div.descripcion ::text").getall()).strip()
```

El selector `::text` con un espacio antes (` ::text`) selecciona el texto de **todos los descendientes**, no solo el texto directo del elemento — muy útil cuando el texto tiene tags anidados como `<b>` o `<span>` en el medio.

## Siguiente paso

Con los datos ya extraídos como diccionarios sueltos, el siguiente paso es estructurarlos formalmente y procesarlos. Continuá con **[04-items-y-pipelines.md](04-items-y-pipelines.md)**.
