import json

def csv_importer():
    return NotImplementedError

def json_importer(file_path):
    with open(file_path, 'r') as read_file:
        news = json.load(read_file)

    return news
