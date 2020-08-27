from parsel import Selector
import requests


URL_BASE = "https://www.tecmundo.com.br/novidades"
next_page_url = '?page=1'


def scrape(number_of_pages=1):
    while number_of_pages > 0:
        response = requests.get(URL_BASE + next_page_url)
        selector = Selector(text=response.text)

        for notice in selector.css(".tec--list__item"):
            title = notice.css(".tec--card__title__link::text").get()
            
            print(title)
        number_of_pages -= 1


scrape()
