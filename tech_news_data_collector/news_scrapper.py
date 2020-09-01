from parsel import Selector
import requests


def fetch_content(url, timeout=1):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        return response.text


def get_all_attributes(url):
    news = []
    title = ''
    content = fetch_content(url)
    selector = Selector(content)
    for new in selector.css("div.z--pt-40.z--pb-24.z--pl-16"):
        title = new.css("h1.tec--article__header__title::text").get()
        print(title)
        return news.append({
            "title": title
        })
    return news


def scrape(page=1):
    all_news = []
    base_url = f"https://www.tecmundo.com.br/novidades?page={page}"
    content = fetch_content(base_url)
    selector = Selector(content)
    for new in selector.css("div.tec--list__item"):
        url = new.css("a.tec--card__title__link::attr(href)").get()
        news = get_all_attributes(url)
        all_news.append(news)
    return all_news


print(scrape())
