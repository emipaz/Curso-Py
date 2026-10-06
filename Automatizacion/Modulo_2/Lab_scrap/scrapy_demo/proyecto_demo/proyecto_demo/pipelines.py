# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ValidarCitaPipeline:
    """Descarta items sin texto o sin autor (control de calidad basico)."""

    def process_item(self, item):
        adapter = ItemAdapter(item)
        if not adapter.get("texto") or not adapter.get("autor"):
            raise DropItem(f"Item incompleto: {item}")
        return item


class ContadorPipeline:
    """Cuenta cuantos items pasaron, solo para mostrar el ciclo de vida del pipeline."""

    total = 0

    def open_spider(self, spider):
        self.total = 0

    def process_item(self, item):
        self.total += 1
        return item

    def close_spider(self, spider):
        spider.logger.info(f"ContadorPipeline: {self.total} items procesados")
