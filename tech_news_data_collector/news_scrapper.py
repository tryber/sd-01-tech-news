from parsel import Selector
import requests


URL_BASE = "https://www.tecmundo.com.br/novidades"


def scrape(number_of_pages=1):
    page_number = 1
    next_url_page = "?page=1"
    while page_number <= number_of_pages:
        response = requests.get(URL_BASE + next_url_page)
        selector = Selector(text=response.text)

        for notice in selector.css(".tec--list__item"):
            title = notice.css(".tec--card__title__link::text").get()
            url = notice.css(".tec--card__title__link::attr(href)").get()

            # Baixa o conteúdo da página de detalhes
            detail_response = requests.get(url)
            detail_selector = Selector(text=detail_response.text)

            timestamp = detail_selector.css("#js-article-date::text").get()
            writer = detail_selector.css(
                ".tec--author__info__link::text"
                ).get()
            shares_count = detail_selector.css(
                ".tec--toolbar__item::text"
                ).get()
            comments_count = detail_selector.css(
                "#js-comments-btn::text"
                ).get().split(' ', 1)
            summary = detail_selector.css(
                ".tec--article__body z--px-16 p402_premium *::text"
                ).get()
            sources = detail_selector.css(".tec--badge::text").getall()
            categories = detail_selector.css(
                ".tec--badge .tec--badge--primary::text"
                ).get()
            print(
                    title,
                    'titulo',
                    '\n',
                    url,
                    'url',
                    '\n',
                    timestamp,
                                     'timestamp',
                    '\n',
                    writer,
                                     'writer',
                    '\n',
                    shares_count,
                                     'shares_count',
                    '\n',
                    comments_count,
                                     'comments_count',
                    '\n',
                    summary,
                                     'summary',
                    '\n',
                    sources,
                                     'sources',
                    '\n',
                    categories,
                                     'categories',
                    '\n',
                )

        page_number += 1
        next_url_page = f"?page={page_number}"


scrape()
