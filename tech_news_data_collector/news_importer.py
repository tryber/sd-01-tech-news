import csv
import service
import bd
from csv import DictReader
import sys


validHeader = ['url', 'title', 'timestamp', 'writer', 'shares_count', 'comments_count', 'summary', 'sources', 'categories']


# def csv_importer(file):
#     validFile(file)
#     cont_save = 0
#     failed = 0
#     with open(file) as csvfile:
#         csv_reader = csv.reader(csvfile)
#         line_count = 0
#         for row in csv_reader:
#             if line_count >= 1:
#                 if valid_notice(row):
#                     value = create_dict(validHeader, row)
#                     bd.save_notice(value)
#                     cont_save += 1
#                 else:
#                     print(f'Erro na notícia {line_count}')
#                     failed += 1
#                     # raise Exception(f'Erro na notícia {line_count}')
#             line_count += 1
#         print(f'Processed {line_count} lines.')
#         print(f'Salvos {cont_save}.')
#         print(f'Failed {failed}.')


# Codigo do Doug https://github.com/tryber/sd-01-tech-news/pull/1/files/ file  tech_news_data_collector/news_importer.py

def csv_importer2(path):
    validFile(path)
    datas = list()
    with open(path, "r", encoding='utf-8-sig') as csv_file:
        readCSV = DictReader(csv_file, delimiter=",")
        for row in readCSV:
            newDic = {key: row[key] for key in row if row[key] != " "}
            # print(newDic)
            if newDic:
                bd.save_notice(newDic)
                print('save')
            datas.append(newDic)
    # print(datas)
    # data = DataPersistence("tech_news", "news", datas)
    # data.f_insert_many_bd()
    print("Importação realizada com sucesso")
    pass

# def create_dict(arr, values):
#     dict_values = {}
#     for i in range(len(arr)):
#         dict_values[arr[i]] = values[i]
#         print(values[i])
#         print(type(values[i]))
#     return dict_values


def valid_notice(dict_notice):
    valid = True
    for value in dict_notice:
        if not value:
            valid = False
            break
    return valid


def validFile(file):
    service.isExist(file)
    service.validTypeFile(file, 'csv')
    service.validHeader(getHeader(file))


def getHeader(file):
    with open(file, encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i = next(reader)
    return i


def init(files='data.csv'):
    try:
        csv_importer2(files)
    except Exception as e:
        print(e, file=sys.stderr)
