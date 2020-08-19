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
            return collections.insert_one(self.data)
        except ValueError as err:
            return f"\033[42mO deu erro: \033[31m {err}\033[0;0m"

    def f_insert_many_bd(self):
        try:
            client = self.client
            db = client[self.db]
            collections = db[self.collections]
            resp = collections.insert_many(self.data, ordered=False)
            if isinstance(resp.inserted_ids, list):
                return True
            return False
        except ValueError as err:
            return f"\033[42mO deu erro: \033[31m {err}\033[0;0m"

    def f_find_One_bd(self):
        try:
            client = self.client
            db = client[self.db]
            collections = db[self.collections]
            return collections.find(self.data)
        except ValueError as err:
            return f"\033[42mO deu erro: \033[31m {err}\033[0;0m"

    def f_find_all_bd(self):
        try:
            client = self.client
            db = client[self.db]
            collections = db[self.collections]
            return collections.find()
        except ValueError as err:
            return f"\033[42mO deu erro: \033[31m {err}\033[0;0m"

    def f_one_and_delete_bd(self):
        try:
            client = self.client
            db = client[self.db]
            collections = db[self.collections]
            return collections.one_and_delete(self.data)
        except ValueError as err:
            return f"\033[42mO deu erro: \033[31m {err}\033[0;0m"

    def f_drop_bd(self):
        try:
            client = self.client
            db = client[self.db]
            collections = db[self.collections]
            return collections.drop()
        except ValueError as err:
            return f"\033[42mO deu erro: \033[31m {err}\033[0;0m"

