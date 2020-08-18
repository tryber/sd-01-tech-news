from csv import DictReader
from pathlib import Path

path = "files_import/news.csv"


def csv_importer(path):
    datas = list()
    with open(path, "r") as csv_file:
        readCSV = DictReader(csv_file, delimiter=";")
        for row in readCSV:
            newDic = {key: row[key] for key in row if row[key] != " "}
            datas.append(newDic)
    return datas

