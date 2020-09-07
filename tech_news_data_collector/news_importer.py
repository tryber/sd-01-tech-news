from pymongo import MongoClient
import json


def csv_importer():
    raise NotImplementedError


def file_exists(path):
    if not path:
        return False
    True


def validate_path_file(path, format):
    array_of_path = path.split(".")
    if array_of_path[1] == format:
        return True
    return False


def json_importer(path_to_file="json_file.json"):
    if file_exists(path_to_file) is False:
        return print(f"Arquivo {path_to_file} não encontrado")

    if validate_path_file(path_to_file, "json") is False:
        return print("Formato inválido")

    with open(path_to_file) as file:
        notices = json.load(file)
        for row in notices:
            if len(row) != 9:
                return print(f"Erro na notícia {row[0]}")

    client = MongoClient()
    db = client.tech_news
    try:
        for notice in notices:
            db.notices.find_one_and_update(
                {"url": notice["url"]}, {"$set": notice}, upsert=True
            )
        client.close()
    except client:
        print(client.errors)
    print("Importação realizada com sucesso")
