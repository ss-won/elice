import pymongo
from pprint import pprint


# 데이터베이스와 컬렉션을 생성하는 코드입니다. 수정하지 마세요!
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["library"]
col = db["books"]

# 데이터를 만들고 삽입하세요.
dt = {"title": "Romeo and Juliet",
      "author": "William Shakespeare", "date_received": "2012-04-01"}
data = col.insert_one(dt)

# 삽입된 데이터 id를 이용해 데이터를 보기 좋게 출력하세요.
cursor = col.find_one({'_id': data.inserted_id})
pprint(cursor)
