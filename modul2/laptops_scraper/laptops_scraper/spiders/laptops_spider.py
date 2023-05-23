import scrapy


class LaptopsSpider(scrapy.Spider):
    name = 'laptops'
    start_urls = ['https://ek.ua/ua/list/298/']

    def parse(self, response):
        products = response.css('.list_form1')
        for product in products:
            model = product.css('.model-short-title a::title').get()
            image_url = product.css('.model-short-img img::attr(src)').get()
            shop = product.css('.model-short-shop span::text').get()
            price = product.css('.model-short-price::text').get()
            yield {
                'model': model,
                'image_url': image_url,
                'shop': shop,
                'price': price,
            }

        next_page = response.css('.paginator .active + a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
