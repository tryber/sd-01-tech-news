from pymongo import MongoClient


class DataPersistence:
    def __init__(self, db=None, collections=None, data=None):
        self.client = MongoClient("localhost", 27017)
        self.db = db or "tech_news"
        self.collections = collections or "news"
        self.data = data

    def f_insert_one_bd(self):
        try:
            client = self.client
            db = client[self.db]
            collections = db[self.collections]
            resp = collections.insert_one(self.data)
            return resp
        except ValueError as err:
            return f"\033[42mO deu erro: \033[31m {err}\033[0;0m"

    def f_insert_many_bd(self):
        try:
            client = self.client
            db = client[self.db]
            collections = db[self.collections]
            resp = collections.insert_many(self.data, ordered=False)
            print("#" * 30)
            print(resp)
            print("#" * 30)
            return resp
        except ValueError as err:
            return f"\033[42mO deu erro: \033[31m {err}\033[0;0m"

    def f_find_bd(self):
        try:
            client = self.client
            db = client[self.db]
            collections = db[self.collections]
            resp = collections.find(self.data,)
            return resp
        except ValueError as err:
            return f"\033[42mO deu erro: \033[31m {err}\033[0;0m"

    def f_one_and_delete_bd(self):
        try:
            client = self.client
            db = client[self.db]
            collections = db[self.collections]
            resp = collections.one_and_delete(self.data,)
            return resp
        except ValueError as err:
            return f"\033[42mO deu erro: \033[31m {err}\033[0;0m"

    def f_drop_bd(self):
        try:
            client = self.client
            db = client[self.db]
            collections = db[self.collections]
            resp = collections.drop()
            return resp
        except ValueError as err:
            return f"\033[42mO deu erro: \033[31m {err}\033[0;0m"

