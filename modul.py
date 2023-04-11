import scrapy


class ModulSpider(scrapy.Spider):
    name = "modul"
    allowed_domains = ["hotline.ua"]
    start_urls = ["http://hotline.ua/"]

    def parse(self, response):
        pass
