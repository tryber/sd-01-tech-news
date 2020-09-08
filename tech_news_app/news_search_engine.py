from pymongo import MongoClient

# Todo o código abaixo foi feito com a ajuda do conrado
# https://github.com/tryber/sd-01-tech-news/tree/conradomedeiros-sd-01-tech-news


def get_data_from_database(search):
    client = MongoClient()
    db = client.tech_news
    array_of_notices = []
    try:
        notices = db.news.find(search, {"_id": 0, "title": 1, "url": 1})
        for notice in notices:
            array_of_notices.append(notice)
        client.close()
        return array_of_notices
    except client:
        return print(client.errors)


def validate_title(title):
    if len(title) == 0:
        return False


def search_by_title(title):
    if validate_title(title) is False:
        return print("Dados inválidos")
    received_data = get_data_from_database(
        {"title": {"$regex": title, "$options": "i"}}
        )
    print("title", received_data)
    return received_data


def validate_date(date):
    if len(date) == 0:
        return []
    splited_date = date.split("/")
    return (
        len(splited_date[0]) == 4
        and len(splited_date[1]) == 2
        and len(splited_date[2]) == 2
    )


def format_date(date):
    replace_date = date.replace("/", "-")
    return replace_date


def search_by_date(date):
    if validate_date(date) is False:
        return print("Data inválida")
    formated_date = format_date(date)
    received_data = get_data_from_database({"timestamp": formated_date})
    print("date", received_data)
    return received_data


def search_by_source(source):
    received_data = get_data_from_database(
        {"sources": {"$regex": f"^{source}", "$options": "i"}}
        )
    print("source", received_data)
    return received_data


def search_by_category(categories):
    received_data = get_data_from_database(
        {"categories": {"$regex": f"^{categories}", "$options": "i"}}
        )
    print("categories", received_data)
    return received_data
