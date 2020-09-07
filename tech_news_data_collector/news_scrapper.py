from parsel import Selector
import requests
import time


def get_all_title(value):
    selector = Selector(value)
    title = selector.css(".tec--article__header__title::text").get().strip()
    return title


def get_all_timestamp(value):
    selector = Selector(value)
    timestamp = selector.css(".tec--timestamp__item::text").get()
    return timestamp


def get_all_writer(value):
    selector = Selector(value)
    writer = selector.css(".tec--author__info__link::text").get()
    if writer:
        return writer.strip()


def get_all_shares_count(value):
    selector = Selector(value)
    shares_count = selector.css(".tec--toolbar__item::text").getall()
    if shares_count:
        return shares_count[1].split(" ")[4]


def get_all_comments_count(value):
    selector = Selector(value)
    comments_count = selector.css(
        "#js-comments-btn::text"
        ).getall()
    if len(comments_count) > 0:
        comments_split = comments_count[1]
        if len(comments_split) > 15:
            return comments_split.split(" ")[6]
        else:
            return comments_split.split(" ")[2]


def get_all_summary(value):
    selector = Selector(value)
    summary = selector.css(".tec--article__body p *::text").getall()
    text_summary = " ".join(summary)
    return text_summary


def get_all_sources(value):
    selector = Selector(value)
    sources = selector.xpath("//a[@class='tec--badge']/text()").getall()
    source_format = get_all(sources)
    return source_format


def get_all_categories(value):
    selector = Selector(value)
    categories = selector.css("#js-categories a::text").getall()
    categories_format = get_all(categories)
    return categories_format


def format_value(value):
    return value.strip()


def get_all(arr):
    if arr:
        source = map(format_value, arr)
        return list(source)
    return arr


# Parte da solução do código do Guilherme https://github.com/tryber/sd-01-tech-news/blob/guiiluiz-tech-news/tech_news_data_collector/news_scrapper.py
def scrape(pages=1):
    page_url = "https://www.tecmundo.com.br/novidades"
    current_page = 1
    news_data = []
    while current_page <= pages:
        response = requests.get(page_url)
        selector = Selector(text=response.text)
        news_url = selector.css(".tec--card__title__link::attr(href)").getall()

        for news in news_url:
            data = get_news_data(news)
            if data:
                news_data.append(data)

        current_page += 1
        page_url = f"https://www.tecmundo.com.br/novidades?page={current_page}"

    print(news_data)
    print('Raspagem de notícias finalizada')


def get_news_data(url):
    success = False
    attempts = 1
    while not success and attempts <= 3:
        response = requests.get(url)
        # Parte da Solução do Henrique Eyer pra verificar o retorno dos dados != None - https://github.com/tryber/sd-01-tech-news/tree/exemplo-tech-news-henriqueeyer
        contentEncoding = response.headers['Content-Encoding']
        success = contentEncoding == 'gzip'
        attempts += 1

        if response.status_code == 404:
            attempts = 4
        elif response.status_code == 429:
            time.sleep(6)
        if success:
            return {
                "url": url,
                "title": get_all_title(response.text),
                "timestamp": get_all_timestamp(response.text),
                "writer": get_all_writer(response.text),
                "shares_count": get_all_shares_count(response.text),
                "comments_count": get_all_comments_count(response.text),
                "summary": get_all_summary(response.text),
                "sources": get_all_sources(response.text),
                "categories": get_all_categories(response.text)
            }


scrape(2)
