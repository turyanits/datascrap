import requests
from bs4 import BeautifulSoup

BASE_URL = "http://www.univ.kiev.ua/"
URL = BASE_URL + "/ua/departments/"

# Мій user agent
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 "
                  "Safari/537.36 "
}

# Завантажуємо вміст сторінки
response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")

# Відкриваємо файл для запису даних
with open("data.txt", "w", encoding='utf-8') as f:
    # Пошук інформації про факультети
    fac_container = soup.find(id="")
    if fac_container is not None:
        for fac in fac_container.find_all("a"):
            txt = fac.text[0::]  # назва факультету без ID
            url = BASE_URL + fac["href"]  # URL факультету
            print(txt)
            print(url)
            f.writelines(txt + "\n")
            f.writelines(url + "\n")

