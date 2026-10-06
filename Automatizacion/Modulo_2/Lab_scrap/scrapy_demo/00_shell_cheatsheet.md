# Scrapy shell — comandos para mostrar en vivo

Abrir (desde cualquier carpeta, con el entorno activado):

```bash
uv run scrapy shell "https://books.toscrape.com"
```

Esto descarga la pagina UNA vez y la deja en la variable `response`, para
poder probar selectores sin volver a pedirla cada vez (al revés de
`requests.get()` + `BeautifulSoup()`, donde si cambiás el selector no hace
falta re-pedir la página, pero tampoco hay nada que te lo recuerde).

Probar en orden:

```python
# Ver la respuesta
response.status
response.url

# Seleccionar todos los libros de la pagina
response.css("article.product_pod")
len(response.css("article.product_pod"))

# Extraer el titulo del PRIMER libro
response.css("h3 a::attr(title)").get()

# Extraer los titulos de TODOS los libros
response.css("h3 a::attr(title)").getall()

# Lo mismo pero con XPath (equivalente)
response.xpath("//h3/a/@title").getall()

# Precio (ojo: viene como texto con el simbolo de moneda)
response.css("p.price_color::text").get()

# Abrir la pagina real en el navegador, para comparar con lo que "ve" Scrapy
view(response)

# Siguiente pagina del catalogo (link de paginacion)
response.css("li.next a::attr(href)").get()

# Salir
exit()
```

## Con quotes.toscrape.com (para la parte de items/tags)

```bash
uv run scrapy shell "https://quotes.toscrape.com"
```

```python
response.css("div.quote")[0].css("span.text::text").get()
response.css("div.quote")[0].css("small.author::text").get()
response.css("div.quote")[0].css("a.tag::text").getall()
```

## Punto para remarcar en la demo

`response.css(...)` / `.xpath(...)` son identicos adentro de un spider y
adentro del shell — por eso conviene *siempre* probar los selectores en el
shell antes de escribirlos en el spider. Evita el ciclo lento de "edito el
spider -> corro todo el crawl -> leo el log -> repito".
