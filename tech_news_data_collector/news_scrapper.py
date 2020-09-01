from parsel import Selector
import requests
import time


def get_news_title(content):
    selector = Selector(content)
    title = selector.css(".tec--article__header__title::text").get()
    return title.strip()


def get_news_timestamp(content):
    selector = Selector(content)
    return selector.css(".tec--timestamp__item").xpath('./time/@datetime').get()


def get_news_writer(content):
    selector = Selector(content)
    author = selector.css(".tec--author__info__link::text").get()
    if author == None:
        writer = selector.xpath("//div[contains(@class, 'tec--timestamp__item') and contains(@class, 'z--font-bold')]").xpath(".//a/text()").get()
        if writer:
            return writer.strip()
        else:
            name = selector.xpath("//p[contains(@class, 'z--m-none') and contains(@class, 'z--truncate') and contains(@class, 'z--font-bold')]/text()").get()
            if name:
                return name.strip()
    return author.strip()


def get_news_shares(content):
    selector = Selector(content)
    shares = selector.css(".tec--toolbar__item::text").getall()
    if shares:
        return shares[1].strip().split(' ')[0]
    else:
        return 0


def get_news_comments(content):
    selector = Selector(content)
    comments = selector.xpath("//button[@id='js-comments-btn']/@data-count").get()
    return comments


def get_news_summary(content):
    selector = Selector(content)
    summary = selector.css(".tec--article__body p").get()
    summary_selector = Selector(summary)
    summary_text = summary_selector.css("*::text").getall()
    return ''.join(summary_text)


def get_news_sources(content):
    selector = Selector(content)
    sources_list = selector.css(".tec--badge::text").getall()
    if sources_list:
        sources = map(lambda text: text.strip(), sources_list)
        return list(sources)


def get_news_categories(content):
    selector = Selector(content)
    categories_list = selector.xpath("//a[contains(@class, 'tec--badge') and contains(@class, 'tec--badge--primary')]/text()").getall()
    if categories_list:
        categories = map(lambda text: text.strip(), categories_list)
        return list(categories)


def get_news_data(url):
    success = False
    attempts = 1
    while not success and attempts <= 3:
        response = requests.get(url)
        contentEncoding = response.headers['Content-Encoding'] # Solução do Henrique Eyer pra verificar o retorno dos dados != None - https://github.com/tryber/sd-01-tech-news/tree/exemplo-tech-news-henriqueeyer
        success = contentEncoding == 'gzip'
        attempts += 1

        if response.status_code == 404:
            attempts = 4
        elif response.status_code == 429:
            time.sleep(6)
        if success:
            return {
                "url": url,
                "title": get_news_title(response.text),
                "timestamp": get_news_timestamp(response.text),
                "writer": get_news_writer(response.text),
                "shares_count": get_news_shares(response.text),
                "comments_count": get_news_comments(response.text),
                "summary": get_news_summary(response.text),
                "sources": get_news_sources(response.text),
                "categories": get_news_categories(response.text)
            }


def scrape(pages = 1):
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

scrape(3)
