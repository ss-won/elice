import pymongo


# 데이터베이스와 컬렉션을 생성하는 코드입니다. 수정하지 마세요!
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["cafe"]
orders = db["menu"]

# brownies의 taste 필드를 추가하세요.
orders.update_one({"item.category": "brownies"}, {"$push": {"taste": "salty"}})

for x in orders.find():
    print(x)
