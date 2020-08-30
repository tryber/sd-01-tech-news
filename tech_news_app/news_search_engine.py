from database.mongo_db import DataPersistence

from datetime import datetime


def search_by_title(search):
    params = {"title": search}
    instan_bd = DataPersistence("tech_news", "news", params)
    data = instan_bd.f_find_One_bd()
    return f"- url: {data[0].get('url')}"


def search_by_date(search):
    params = {"timestamp": datetime.strptime(search, "%d/%m/%Y")}
    instan_bd = DataPersistence("tech_news", "news", params)
    data = instan_bd.f_find_many_bd()
    return data or []


def search_by_source(search):
    params = {"sources": search}
    instan_bd = DataPersistence("tech_news", "news", params)
    data = instan_bd.f_find_One_bd()
    return f"- url: {data[0].get('url')}"


def search_by_category(search):
    params = {"categories": search}
    instan_bd = DataPersistence("tech_news", "news", params)
    data = instan_bd.f_find_One_bd()
    return f"- url: {data[0].get('url')}"
