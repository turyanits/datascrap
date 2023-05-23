import scrapy


class LaptopsSpider(scrapy.Spider):
    name = 'laptops'
    start_urls = ['https://ek.ua/ua/list/298/']

    def parse(self, response):
        laptops = response.css('.model-short-block')
        for laptop in laptops:
            model = laptop.css('.model-conf-title::text').get()
            image_url = laptop.css('.model-short-photo img::attr(src)').get()
            shop = laptop.css('.model-shop-title::text').get()
            price = laptop.css('. model-price-range::text').get()

            yield {
                'Модель': model,
                'URL зображення': image_url,
                'Магазин': shop,
                'Ціна': price
            }
