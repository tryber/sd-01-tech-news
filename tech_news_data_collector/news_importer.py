import csv
import service
import bd


validHeader = ['url', 'title', 'timestamp', 'writer', 'shares_count', 'comments_count', 'summary', 'sources', 'categories']


def csv_importer(file):
    validFile(file)
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile)
        line_count = 0
        for row in csv_reader:
            if line_count >= 1:
                if valid_notice(row):
                    value = create_dict(validHeader, row)
                    bd.save_notice(value)
                else:
                    print(f'Erro na notícia {line_count}')
                    # raise Exception(f'Erro na notícia {line_count}')
            line_count += 1
        print(f'Processed {line_count} lines.')


def create_dict(arr, values):
    dict_values = {}
    for i in range(len(arr)):
        dict_values[arr[i]] = values[i]
    return dict_values


def valid_notice(dict_notice):
    valid = True
    count = 0
    for value in dict_notice:
        if not value:
            valid = False
            print(value, count)
            break
        count += 1
    return valid


def validFile(file):
    service.isExist(file)
    service.validTypeFile(file, 'csv')
    service.validHeader(getHeader(file))


def getHeader(file):
    with open(file, encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i = next(reader)
        print(i)
    return i


def init(file='data.csv'):
    try:
        csv_importer('data.csv')
    except Exception as e:
        print(e)

init()
# def json_importer():
#     raise NotImplementedError
