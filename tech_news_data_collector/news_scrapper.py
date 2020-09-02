from parsel import Selector
import requests
from pymongo import MongoClient


URL_BASE = "https://www.tecmundo.com.br/novidades"


def scrape(number_of_pages=1):
    page_number = 1
    next_url_page = "?page=1"
    array_of_notices = []
    while page_number <= number_of_pages:
        try:
            response = requests.get(URL_BASE + next_url_page)
            response.raise_for_status()
        except (requests.ReadTimeout, requests.HTTPError):
            return print(requests.HTTPError)

        selector = Selector(text=response.text)

        for notice in selector.css(".tec--list__item"):
            url = notice.css(".tec--card__title__link::attr(href)").get()

            try:
                detail_response = requests.get(url)
                detail_response.raise_for_status()
            except (requests.ReadTimeout, requests.HTTPError):
                return print(requests.HTTPError)

            detail_selector = Selector(text=detail_response.text)

            title = detail_selector.css(
                ".tec--article__header__title::text"
                ).get()
            timestamp = selector.css(
                ".tec--timestamp__item::text"
                ).get()
            writer = detail_selector.css(
                ".tec--author__info__link::text"
                ).get()
            if writer:
                writer = writer.strip()
            shares_count = detail_selector.css(
                ".tec--toolbar__item::text"
                ).getall()
            if shares_count and shares_count[1].split(" ")[4]:
                shares_count = shares_count[1].split(" ")[4]
            comments_count = detail_selector.css(
                "#js-comments-btn::text"
                ).getall()
            if comments_count and comments_count[1]:
                comments_count = comments_count[1].split(" ")[1]
            summary = detail_selector.css(
                ".tec--article__body p *::text"
                ).getall()
            text_summary = " ".join(summary)
            sources_to_format = detail_selector.xpath(
                "//a[@class='tec--badge']/text()"
                ).getall()
            sources = get_all(sources_to_format)
            categories_to_format = detail_selector.css(
                "#js-categories a::text"
                ).getall()
            categories = get_all(categories_to_format)

            dict_data = {
                'url': url,
                'title': title,
                'timestamp': timestamp,
                'writer': writer,
                'shares_count': shares_count,
                'comments_count': comments_count,
                'summary': summary,
                'text_summary': text_summary,
                'sources': sources,
                'categories': categories,
                }

            if validate_data_exists(dict_data) is True:
                array_of_notices.append(dict_data)

        page_number += 1
        next_url_page = f"?page={page_number}"

    client = MongoClient()
    db = client.tech_news

    try:
        for notice in array_of_notices:
            db.notices.find_one_and_update(
                {"url": notice['url']},
                {"$set": notice},
                upsert=True
                )
        client.close()
    except (RuntimeError, TypeError, NameError):
        return print(RuntimeError, TypeError, NameError)
    print("Raspagem de notícias finalizada")


def validate_data_exists(obj):
    for element in obj:
        if obj[element] is None:
            return False
    return True


def format_value(value):
    return value.strip()


def get_all(arr):
    if arr:
        source = map(format_value, arr)
        return list(source)
    return arr


scrape()
