# Ejemplo 1: el spider mas chico posible, SIN crear un proyecto Scrapy.
#
# Se corre con "scrapy runspider", no con "python archivo.py" (Scrapy necesita
# su propio reactor/event loop para manejar las requests async).
#
# Correr desde esta carpeta:
#   uv run scrapy runspider 01_mini_spider.py -o libros.json
#
# Que mirar:
# - No hay "while" ni loops manuales pidiendo paginas: Scrapy maneja el
#   descargado por nosotros.
# - "parse" recibe la respuesta YA DESCARGADA (como el .text de requests,
#   pero Scrapy se encargo de la request).
# - "yield" en vez de "return": el spider puede entregar muchos items (y
#   tambien nuevas requests) como un generador.
import scrapy


class LibrosSpider(scrapy.Spider):
    name = "libros"
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for libro in response.css("article.product_pod"):
            # ::text trae varios nodos de texto (hay un <i> en medio),
            # por eso se juntan todos y se colapsan los espacios.
            textos_disponibilidad = libro.css("p.instock.availability::text").getall()
            disponibilidad = " ".join("".join(textos_disponibilidad).split())

            yield {
                "titulo": libro.css("h3 a::attr(title)").get(),
                "precio": libro.css("p.price_color::text").get(),
                "disponibilidad": disponibilidad,
            }
