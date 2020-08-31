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
        print(f"Arquivo {path_to_file} não encontrado")

    with open(path_to_file) as file:
        file_status = csv.reader(file, delimiter=",")
        header, *data = file_status

    intersection = set(header) & set(necessary_headers)

    if(len(intersection) != 9):
        print("Cabeçalho inválido")

    for row in data:
        if(len(row) != 9):
            print(f"Erro na notícia {row[0]}")

    client = MongoClient()
    db = client.tech_news
    try:
        db.notices.updateMany(data, upsert=True)
        client.close()
    except client:
        print(client.errors)

    print("Importação realizada com sucesso")


def json_importer():
    raise NotImplementedError
