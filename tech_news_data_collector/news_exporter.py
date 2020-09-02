import bd
import service
import sys


def csv_exporter():
    try:
        data = bd.data_return()
        service.createFile(data, 'csv', 'item')
        print('Exportação realizada com sucesso')
    except Exception as e:
        print(e, file=sys.stderr)


def json_exporter():
    try:
        data = bd.data_return()
        service.createFile(data, 'json', 'item')
        print('Exportação realizada com sucesso')
    except Exception as e:
        print(e, file=sys.stderr)
