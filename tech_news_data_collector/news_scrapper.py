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


def scrape(page=1):
    base_url = f"https://www.tecmundo.com.br/novidades?page={page}"
    news = []
    content = fetch_content(base_url)
    selector = Selector(content)
    for new in selector.css("div.tec--list__item"):
        url = new.css("a.tec--card__title__link::attr(href)").get()
        title = new.css("a.tec--card__title__link::text").get()
        timestamp = new.css(
            "div.tec--timestamp__item.z--font-semibold::text"
        ).get()
        news.append({
            "url": url,
            "title": title,
            "timestamp": timestamp
        })
    return news


print(scrape(2))
