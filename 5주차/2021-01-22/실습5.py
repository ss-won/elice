import pymongo

# 데이터베이스와 Collection을 생성하는 코드입니다. 수정하지 마세요!
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["profile"]
col = db["people"]

# people Collection에서 지시사항 조건에 맞게 출력하세요.
q = {"results": {"$elemMatch": {"product": "xyz", "score": {"$gte": 8}}}}
for doc in col.find(q):
    print(doc)