import pymongo


# 데이터베이스와 컬렉션을 생성하는 코드입니다. 수정하지 마세요!
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["cafe"]
col1 = db["orders"]
col2 = db["inventory"]

# inventory_docs 필드를 추가하여 작성하세요.
pipeline = [
    {
        "$lookup": {
            "from": "inventory",
            "localField": "item",
            "foreignField": "store",
            "as": "inventory_docs",
        }
    }
]

for x in col1.aggregate(pipeline):
    print(x)
