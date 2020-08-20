import pandas as pd

from database.mongo_db import DataPersistence

from json import dump


def csv_exporter(path):
    if not path:
        return f"Arquivo {path} não encontrado"
    data = DataPersistence()
    datas = data.f_find_all_bd()
    df = pd.DataFrame(datas)
    export_csv = df.to_csv(path, index=None, header=True)
    return export_csv


def json_exporter(path):
    if not path:
        return f"Arquivo {path} não encontrado"
    data = DataPersistence()
    datas = data.f_find_all_bd()
    with open(path, "w") as write_file:
        dump(datas, write_file)
    print("Importação realizada com sucesso")
    pass
