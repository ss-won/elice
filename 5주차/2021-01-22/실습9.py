import pymongo


# 데이터베이스와 컬렉션을 생성하는 코드입니다. 수정하지 마세요!
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["cafe"]
orders = db["menu"]

# brownies의 nickName 필드를 제거하세요.
orders.update_one({"item.category": "brownies"}, {"$unset": {"nickName": 1}})

for x in orders.find():
    print(x)
