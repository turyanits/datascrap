import scrapy
import json
from bs4 import BeautifulSoup

class WashingSpider(scrapy.Spider):
    name = "washing"
    allowed_domains = ["hotline.ua"]
    start_urls = [f"https://hotline.ua/ua/bt/posudomoechnye-mashiny/?p={page}" for page in range(1, 3)]

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        items = soup.find(name="div", class_="list-body__content").find_all(class_="list-item")

        result = []

        for item in items:
            name = item.find(name="a", class_="list-item__title").find(string=True, recursive=False).strip()
            shop_name = item.find(name="a", class_="line-part").find(string=True, recursive=False).strip()
            url = item.find(name="a", class_="list-item__title").get("href")
            price = item.find(class_="price__value").find(string=True, recursive=False)
            image_url = item.find(name="img").get("src")

            result.append({
                "name": name,
                "shop_name": shop_name,
                "price": price,
                "url": url,
                "image_url": image_url
            })

        if result:
            with open("result.json", "w") as f:
                json.dump(result, f, ensure_ascii=False)
        else:
            print("No results found.")