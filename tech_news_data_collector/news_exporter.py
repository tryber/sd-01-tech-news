import json
from pymongo import MongoClient
import csv


necessary_headers = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    "sources",
    "categories"
]


def csv_exporter(path_to_file="teste.csv"):
    if not validate_path_file(path_to_file, "csv"):
        return print("Formato inválido")

    notices = get_data_from_database()
    with open(f"{path_to_file}", "w") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(necessary_headers)
        for notice in notices:
            array_of_elements = []
            for header in necessary_headers:
                array_of_elements.append(notice[header])
            writer.writerow(array_of_elements)
    print("Exportação realizada com sucesso")


def json_exporter(path_to_file="teste.json"):
    if not validate_path_file(path_to_file, "json"):
        return print("Formato inválido")

    notices = get_data_from_database()

    with open(f"{path_to_file}", "w") as file:
        json.dump(notices, file)
    print("Exportação realizada com sucesso")


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
        notices = db.notices.find({}, {"_id": 0})
        for notice in notices:
            array_of_notices.append(notice)
        client.close()
        return array_of_notices
    except client:
        return print(client.errors)
