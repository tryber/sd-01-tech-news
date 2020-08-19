import pandas as pd

from database.mongo_db import DataPersistence


def csv_exporter(path):
    if not path:
        return f"Arquivo {path} não encontrado"
    data = DataPersistence()
    cursor = data.f_find_all_bd()
    df = pd.DataFrame(cursor)
    export_csv = df.to_csv(path, index=None, header=True)
    return export_csv
