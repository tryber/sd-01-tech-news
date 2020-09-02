import os.path
import json
import csv

valid_Header = ['url', 'title', 'timestamp', 'writer', 'shares_count', 'comments_count', 'summary', 'sources', 'categories']


def validHeader(header, verifyArray=valid_Header):
    isValid = True
    for key in verifyArray:
        isContain = key in header
        if not isContain:
            isValid = False
            break
    if isValid:
        print('Cabeçario valido')
    else:
        raise Exception('Cabeçalho inválido')
    return isValid


def isExist(file):
    if os.path.exists(file):
        print(f'Arquivo {file} encontrado!')
    else:
        raise Exception(f'Arquivo {file} não encontrado!')


def validTypeFile(file, typeFile):
    if not len(file.split('.')) == 2:
        raise Exception('Formato inválido')
    if not file.split('.')[1] == typeFile:
        raise Exception('Formato inválido')
    return True


def createFile(value, doc, name):
    name_string = f'{name}.{doc}'
    if doc == 'json':
        with open(name_string, 'w', encoding='utf-8-sig') as outfile:
            json.dump(value, outfile, indent=4, separators=(',', ': '), ensure_ascii=False)
    if doc == 'csv':
        with open(name_string, 'w', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=valid_Header)
            writer.writeheader()
            for item in value:
                writer.writerow(item)


def transform_arr(value):
    print(value)
    str1 = value.replace(']', '').replace('[', '')
    lastValue = str1.replace('"', '').replace("'", "").replace(", ", ",").split(",")
    for item in lastValue:
        print(item)
        item = item.strip()
    return lastValue
