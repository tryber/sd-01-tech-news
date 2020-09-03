from pymongo import MongoClient


def format_date(date):
    splited_date = date.split("/")
    if list(splited_date[2])[0] == "0":
        splited_date[2] = splited_date[2].replace("0", "")
    if list(splited_date[1])[0] == "0":
        splited_date[1] = splited_date[1].replace("0", "")
    return f"{splited_date[2]}/{splited_date[1]}/{splited_date[0]}"


def validate_date(date):
    splited_date = date.split("/")
    return (
        len(splited_date[0]) == 4
        and len(splited_date[1]) == 2
        and len(splited_date[2]) == 2
    )


def get_data_from_database(search):
    client = MongoClient()
    db = client.tech_news
    array_of_notices = []
    try:
        notices = db.notices.find(search, {"_id": 0, "title": 1, "url": 1})
        for notice in notices:
            array_of_notices.append(notice)
        client.close()
        return array_of_notices
    except client:
        return print(client.errors)


def search_by_title():
    return ""


def search_by_date(date):
    if validate_date(date) is False:
        return print("Data inválida")
    formated_date = format_date(date)
    print(formated_date)
    received_data = get_data_from_database({"timestamp": formated_date})
    return received_data


def search_by_source():
    raise NotImplementedError


def search_by_category():
    raise NotImplementedError


search_by_date("2020/09/03")
