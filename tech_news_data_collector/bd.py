from pymongo import MongoClient
from pymongo.collection import ReturnDocument
import service

client = MongoClient('localhost', 27017)
projection_obj = {'_id': True, "url": True, "title": True, "timestamp": True, "writer": True, "shares_count": True, "comments_count": True, "summary": True, "sources": True, "categories": True}
projection_obj2 = {'_id': False, "url": True, "title": True, "timestamp": True, "writer": True, "shares_count": True, "comments_count": True, "summary": True, "sources": True, "categories": True}


def save_notice(data, test=False):
    data['categories'] = service.transform_arr(data['categories'])
    data['sources'] = service.transform_arr(data['sources'])
    bd = client['tech_news']
    if test:
        bd = client['tech_news_test']
    notice = bd.notices
    notice_data = notice.find_one_and_update(
      {'title': data['title']},
      {'$set': data},
      projection=projection_obj,
      upsert=True,
      return_document=ReturnDocument.AFTER
      )
    # notice_data = notice.insert_one(data)
    return notice_data


def data_return():
    allData = []
    bd = client['tech_news']
    notice = bd.notices
    notice_data = notice.find(projection=projection_obj2)
    for doc in notice_data:
        allData.append(doc)
    return allData
