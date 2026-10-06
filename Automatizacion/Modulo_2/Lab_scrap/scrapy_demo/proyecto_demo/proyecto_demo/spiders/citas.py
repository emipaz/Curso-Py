import scrapy

from proyecto_demo.items import CitaItem


class CitasSpider(scrapy.Spider):
    name = "citas"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for cita in response.css("div.quote"):
            yield CitaItem(
                texto=cita.css("span.text::text").get(),
                autor=cita.css("small.author::text").get(),
                tags=cita.css("a.tag::text").getall(),
            )

        siguiente = response.css("li.next a::attr(href)").get()
        if siguiente:
            yield response.follow(siguiente, callback=self.parse)
