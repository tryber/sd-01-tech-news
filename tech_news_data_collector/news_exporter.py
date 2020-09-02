import json
from pymongo import MongoClient


def csv_exporter():
    raise NotImplementedError


def json_exporter(path_to_file="teste.json"):
    if not validate_path_file(path_to_file, "json"):
        return print("Formato inválido")

    client = MongoClient()
    db = client.tech_news
    array_of_notices = []
    try:
        notices = db.notices.find({})
        for notice in notices:
            notice["_id"] = str(notice["_id"]).split("'")[0]
            array_of_notices.append(notice)
        client.close()
    except client:
        return print(client.errors)
    with open(f"{path_to_file}", "w") as file:
        json.dump(array_of_notices, file)
    print("Exportação realizada com sucesso")


def validate_path_file(path, format):
    array_of_path = path.split(".")
    if array_of_path[1] == format:
        return True
    return False


json_exporter()
