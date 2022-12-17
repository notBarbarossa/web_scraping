import requests
from bs4 import BeautifulSoup as bs
from time import sleep

headers = {"User-Agent": "TuneIn Radio/24.6.0; iPhone11,8; iOS/16.2"}

for count in range(1,8):
    sleep(3)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

    response = requests.get(url, headers=headers)

    soup = bs(response.text , "lxml")

    data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

    for i in data:

        name = i.find("h4", class_="card-title").text
        price = i.find("h5").text

        print(name)
        print(price)
















