# -*- coding: utf-8 -*-
import requests

from bs4 import BeautifulSoup

from database.mongo_db import DataPersistence


"""
Detalhe da importação relativo
..database.mongo_db
"""

""" 
importação absoluta
from database.mongo_db 

"""


vermelho = "\033[31m"
verde = "\033[32m"

url = "https://www.tecmundo.com.br/novidades?page="

""" Essa função faz as chamadas de acordo com a
    quantidade de paginas passada como argumento"""

# def input_pages_map(url):
#     print('Quantas paginas tem? ')
#     resp = int(input())
#     links = []
#     for lopps in range(1, resp + 1):
#         try:
#             res = requests.get(url=url+str(lopps))
#             res.raise_for_status()
#             soup = BeautifulSoup(res.text, features="html.parser")
#             for a in soup.find_all("a", href=True):
#                 links.append(a["href"])
#         except Exception as exc:
#             error_in_output(exc, "map_articles")
#     return list(filter(lambda x: x[-3:] == "htm", links))


def clear(value):
    data = []
    for v in value:
        data.append(v.getText())
    return data


def error_in_output(exc, name):
    err = f"""
    {verde}nome da função: {name}
    {vermelho}Error na função map_articles! {exc}
    """
    return err


def map_articles(url):
    try:
        res = requests.get(url=url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, features="html.parser")
        links = [a["href"] for a in soup.find_all("a", href=True)]
        return list(filter(lambda x: x[-3:] == "htm", links))
    except Exception as exc:
        error_in_output(exc, "map_articles")


"""
será que no bs4 tem um
select firts or select one para pegar o primeiro elemento do array?
"""


def creat_(expression_list):
    answer = []
    for url in expression_list:
        try:
            res = requests.get(url=url)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, features="html.parser")

            title = soup.select("#js-article-title")
            date = soup.select("#js-article-date")
            writer = soup.select(".tec--author__info__link")
            shares_count = soup.select(".tec--toolbar__item")
            comments_count = soup.select("#js-comments-btn")
            summary = soup.select(".tec--article__body")
            sources = soup.select(".z--mb-16.z--px-16")
            categories = soup.select("#js-categories")

            obj = {
                "url": url,
                "title": title[0].getText(),
                "timestamp": date[0].getText(),
                "writer": writer[0].getText(),
                "shares_count": shares_count[0].getText(),
                "comments_count": comments_count[0].getText(),
                "summary": summary[0].getText(),
                "sources": clear(sources),
                "categories": clear(categories),
            }

            answer.append(obj)

        except Exception as exc:
            error_in_output(exc, "creat_")
            break
    return answer


def scrape():
    first_pages = map_articles(url)
    data = creat_(first_pages)
    mongo = DataPersistence("tech_news", "news", data)
    resp = mongo.f_insert_many_bd()
    if resp:
        print("Raspagem de notícias finalizada!")
        return resp
    return resp
