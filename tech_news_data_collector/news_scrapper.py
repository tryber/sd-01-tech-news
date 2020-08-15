# -*- coding: utf-8 -*-
import requests

from bs4 import BeautifulSoup

url = "https://www.tecmundo.com.br/novidades"

vermelho = "\033[31m"
verde = "\033[32m"
# azul = "\033[34m"


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


teste = creat_(map_articles(url))
print("*+=" * 45)
print(len(teste))
print(teste)
print("*+=" * 45)
# try:
#     res = requests.get(url=url)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, features="html.parser")
#     links = [a["href"] for a in soup.find_all("a", href=True)]

#     list_articles = soup.select(".tec--card__thumb__link")

#     links = [a["href"] for a in soup.find_all("a", href=True)]

#     links_fatiader = list(filter(lambda x: x[-3:] == "htm", links))

#     print(f"Total de artigos: {str(len(links_fatiader))}")
#     print(links_fatiader)
#     print(f"primeira tag: {str(list_articles)}")
#     print(list_articles[0].getText())
# except Exception as exc:
#     print("*" * 30)
#     print(f"Houve um erro: {exc}")
#     print("*" * 30)
# else:
#     pass

# def scrape():
#     raise NotImplementedError
