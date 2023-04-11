from requests import get
from bs4 import BeautifulSoup


BASE_URL = "https://www.univ.kiev.ua/"
URL = f"{BASE_URL}/ua/departments"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
FILE_NAME = "data.txt"
with open(FILE_NAME, "w", encoding="utf-8") as file:

    page = get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content,  "html.parser")
    fac_list = soup.find(class_="b-references__holder")
    for li in fac_list.find_all("li"):
        a = li.find("a")
        fac_name = a.find(string=True, recursive=False)
        fac_url = BASE_URL + a.get("href")

        print(f"Назва факультету: {fac_name}\nURL: {fac_url}")
        file.write(f"Назва факультету: {fac_name}\n")
        file.write(f"URL: {fac_url}\n")
        # завантажуємо сторінку факультету
        fac_page = get(fac_url, headers=HEADERS)
        soup = BeautifulSoup(fac_page.content, "html.parser")

        # знаходимо список кафедр
        dep_list = soup.find("ol")

        # для кожної кафедри у списку
        if dep_list:
            for li in dep_list.find_all("li", class_="b-body__text"):
                dep_name = li.text.strip()
                print(dep_name)
                file.write(f"    Назва кафедри: {dep_name}\n")
        else:
            print("Список кафедр не знайдено")
