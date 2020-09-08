from pymongo import MongoClient

# Todo o código abaixo foi feito com a ajuda do conrado
# https://github.com/tryber/sd-01-tech-news/tree/conradomedeiros-sd-01-tech-news


def get_data_from_database(search):
    client = MongoClient()
    db = client.tech_news
    array_of_notices = []
    try:
        notices = db.news.find(search, {"_id": 0, "title": 1, "url": 1})
        print("notices", notices)
        for notice in notices:
            array_of_notices.append(notice)
        client.close()
        return array_of_notices
    except client:
        return print(client.errors)


def validate_title(title):
    if len(title) == 0:
        return []


def search_by_title(title):
    if validate_title(title) == []:
        return print("dados invalidos")
    received_data = get_data_from_database(
        {"title": {"$regex": title, "$options": "i"}}
        )
    print("title", received_data)
    return received_data
