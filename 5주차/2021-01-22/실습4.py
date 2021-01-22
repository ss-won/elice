import pymongo

# 데이터베이스와 Collection을 생성하는 코드입니다. 수정하지 마세요!
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["profile"]
col = db["people"]

# prople Collection에 들어있는 책들을 출력하세요.
p = {"_id": {"$mod": [2, 0]}}

for doc in col.find(p):
    print(doc)