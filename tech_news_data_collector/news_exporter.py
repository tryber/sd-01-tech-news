import bd
import service
import json


def csv_exporter():
    data = bd.data_return()
    service.createFile(data, 'csv', 'item')
    print('Exportação realizada com sucesso')


def json_exporter():
    data = bd.data_return()
    service.createFile(data, 'json', 'item')
    print('Exportação realizada com sucesso')
