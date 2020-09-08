from pymongo import MongoClient
import json
import sys

# Código feito com ajuda do conrado!
# https://github.com/tryber/sd-01-tech-news/tree/conradomedeiros-sd-01-tech-news


def csv_exporter():
    raise NotImplementedError


def validate_path_file(path, format):
    array_of_path = path.split(".")
    if array_of_path[1] == format:
        return True
    return False


def get_data_from_database():
    client = MongoClient()
    db = client.tech_news
    array_of_notices = []
    try:
        notices = db.news.find({}, {"_id": 0})
        for notice in notices:
            array_of_notices.append(notice)
        client.close()
        return array_of_notices
    except Exception as e:
        print(e, file=sys.stderr)


def json_exporter(path_to_file="tech_news.json"):
    if not validate_path_file(path_to_file, "json"):
        return print("Formato inválido")

    notices = get_data_from_database()

    with open(f"{path_to_file}", "w") as file:
        json.dump(notices, file)
    print("Exportação realizada com sucesso")
