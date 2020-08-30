from database.mongo_db import DataPersistence


def top_5_news():
    instan_bd = DataPersistence()
    data = instan_bd.f_find_all_bd().sort("shares_coun", direction="DESCENDING")
    value = [f"- url: {data[order].get('url')}" for order in range(0, 5)]
    return value


def top_5_categories():
    raise NotImplementedError
