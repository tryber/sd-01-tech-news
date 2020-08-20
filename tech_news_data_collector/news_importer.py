from csv import DictReader

from database.mongo_db import DataPersistence

import pandas as pd


def csv_importer(path):
    print(path)
    if not path:
        return f"Arquivo {path} não encontrado"
    datas = list()
    with open(path, "r") as csv_file:
        readCSV = DictReader(csv_file, delimiter=",")
        for row in readCSV:
            newDic = {key: row[key] for key in row if row[key] != " "}
            datas.append(newDic)
    data = DataPersistence("tech_news", "news", datas)
    data.f_insert_many_bd()
    print("Importação realizada com sucesso")
    pass


def json_importer(path):
    if not path:
        return f"Arquivo {path} não encontrado"
    file_json = pd.read_json(path)
    data = DataPersistence("tech_news", "news", file_json)
    data.f_insert_many_bd()
    print("Importação realizada com sucesso")
    pass

