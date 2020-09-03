import csv
from pymongo import MongoClient
import json


necessary_headers = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    "sources",
    "categories",
]


def csv_importer(path_to_file="teste.csv"):
    if file_exists(path_to_file) is False:
        return print(f"Arquivo {path_to_file} não encontrado")

    if validate_path_file(path_to_file, "csv") is False:
        return print("Formato inválido")

    with open(path_to_file) as file:
        file_status = csv.reader(file, delimiter=";")
        header, *data = file_status

    intersection = set(header) & set(necessary_headers)

    if len(intersection) != 9:
        print(intersection)
        return print("Cabeçalho inválido")

    number_line = 1
    for row in data:
        if len(row) != 9:
            return print(f"Erro na notícia {number_line}")
        number_line += 1

    array_formated = formate_arrays(data)
    client = MongoClient()
    db = client.tech_news
    try:
        for notice in array_formated:
            db.notices.find_one_and_update(
                {"url": notice["url"]}, {"$set": notice}, upsert=True
            )
        client.close()
    except client:
        print(client.errors)

    print("Importação realizada com sucesso")


def formate_arrays(array):
    array_of_objects = []
    for line in array:
        newObj = {
            "url": line[0],
            "title": line[1],
            "timestamp": line[2],
            "writer": line[3],
            "shares_count": line[4],
            "comments_count": line[5],
            "summary": line[6],
            "sources": line[7],
            "categories": line[8],
        }
        array_of_objects.append(newObj)
    return array_of_objects


def file_exists(path):
    if not path:
        return False
    True


def validate_path_file(path, format):
    array_of_path = path.split(".")
    if array_of_path[1] == format:
        return True
    return False


def json_importer(path_to_file="teste.json"):
    if file_exists(path_to_file) is False:
        return print(f"Arquivo {path_to_file} não encontrado")

    if validate_path_file(path_to_file, "json") is False:
        return print("Formato inválido")

    with open(path_to_file) as file:
        notices = json.load(file)
        for row in notices:
            if len(row) != 9:
                print(len(row))
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


csv_importer()
