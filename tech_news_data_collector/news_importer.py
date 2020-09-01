import csv
from pymongo import MongoClient

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


def csv_importer(path_to_file):
    if not path_to_file:
        return print(f"Arquivo {path_to_file} não encontrado")

    if path_to_file.split(".")[2] != "csv":
        return print("Formato inválido")

    with open(path_to_file) as file:
        file_status = csv.reader(file, delimiter=",")
        header, *data = file_status

    intersection = set(header) & set(necessary_headers)

    if(len(intersection) != 9):
        return print("Cabeçalho inválido")

    for row in data:
        if(len(row) != 9):
            return print(f"Erro na notícia {row[0]}")

    array_formated = formate_arrays(data)
    client = MongoClient()
    db = client.tech_news
    try:
        db.notices.updateMany(array_formated, upsert=True)
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
            "categories": line[8]
            }
        array_of_objects.append(newObj)
    return array_of_objects


def json_importer():
    raise NotImplementedError
