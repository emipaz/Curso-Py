# Ejemplo 2: seguir enlaces (paginacion) + entrar a cada pagina de detalle.
#
# Esto es lo que mas distingue a Scrapy de un script bs4+requests: no hace
# falta armar un loop manual tipo "while hay pagina siguiente: requests.get(...)".
# El spider simplemente "yield"-ea nuevas requests y Scrapy las encola,
# descarga en paralelo (segun CONCURRENT_REQUESTS) y las despacha al callback
# que le indiquemos.
#
# Correr desde esta carpeta (el -a paginas=N limita cuantas paginas de catalogo
# recorre, para la demo en vivo no queremos barrer las 50 paginas):
#   uv run scrapy runspider 02_spider_paginacion.py -a paginas=2 -o libros_detalle.jsonl
import scrapy


class LibrosDetalleSpider(scrapy.Spider):
    name = "libros_detalle"
    start_urls = ["https://books.toscrape.com"]

    custom_settings = {
        "DOWNLOAD_DELAY": 0.3,
        "AUTOTHROTTLE_ENABLED": True,
    }

    def __init__(self, paginas=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.paginas_max = int(paginas)
        self.paginas_vistas = 0

    def parse(self, response):
        self.paginas_vistas += 1

        for libro in response.css("article.product_pod"):
            url_detalle = libro.css("h3 a::attr(href)").get()
            # response.follow resuelve la URL relativa automaticamente
            # (no hace falta response.urljoin a mano).
            yield response.follow(url_detalle, callback=self.parse_detalle)

        siguiente = response.css("li.next a::attr(href)").get()
        if siguiente and self.paginas_vistas < self.paginas_max:
            yield response.follow(siguiente, callback=self.parse)

    def parse_detalle(self, response):
        rating_texto = response.css("p.star-rating::attr(class)").get() or ""
        rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating_num = next((v for k, v in rating_map.items() if k in rating_texto), None)

        yield {
            "titulo": response.css("h1::text").get(),
            "precio": response.css("p.price_color::text").get(),
            "rating": rating_num,
            "url": response.url,
        }
