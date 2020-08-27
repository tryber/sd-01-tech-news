from parsel import Selector
import requests


URL_BASE = "https://www.tecmundo.com.br/novidades"
# Define a primeira página como próxima a ter seu conteúdo recuperado


def scrape():
    next_page_url = 'pagina=1'
    while next_page_url:
        # Busca o conteúdo da próxima página
        response = requests.get(URL_BASE + next_page_url)
        selector = Selector(text=response.text)
        # Imprime os produtos de uma determinada página
        for notice in selector.css("tec--list__item"):
            title = notice.css("tec--card__title::text").get()
            timestamp = notice.css("tec--timestamp__item::text").get()

        # # Busca o detalhe de um produto
        # page_href = notice.css("tec--card__title__link::attr(href)").get()
        # page_url = page_href

        # # Baixa o conteúdo da página de detalhes
        # page_response = requests.get(page_url)
        # page_selector = Selector(text=page_response.text)

        # url = page_url
        # writer = notice.css("tec--author__info__link a::text").get()
        # shares_count = notice.css("tec--toolbar__item[0]::text").get()
        # comments_count = notice.css("js-comments-btn::attr(data-count)").get()
        # summary = notice.css("tec--card__title::text").get()
        # sources = notice.css("tec--badge a::text").get()
        # categories = notice.css("tec--card__title::text").get()
        # Extrai a descrição do produto
        print(

            "title", title,
            "timestamp", timestamp,
            # "url", url,
            # "writer", writer,
            # "shares_count", shares_count,
            # "comments_count", comments_count,
            # "summary", summary,
            # "sources", sources,
            # "categories", categories
        )

        # Descobre qual é a próxima página
        next_page_url = selector.css(".next a::attr(href)").get()


scrape()
