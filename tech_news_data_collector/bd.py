from pymongo import MongoClient
from pymongo.collection import ReturnDocument

client = MongoClient('localhost', 27017)
projection_obj = {'_id': True, "url": True, "title": True, "timestamp": True, "writer": True, "shares_count": True, "comments_count": True, "summary": True, "sources": True, "categories": True}


def save_notice(data, test=False):
    bd = client['tech_news']
    if test:
        bd = client['tech_news_test']
    notice = bd.notices
    notice_data = notice.find_one_and_update(
      {'title': data['title']},
      {'$set': data},
      projection=projection_obj,
      upsert=True,
      return_document=ReturnDocument.AFTER)
    return notice_data
