import pymongo


# 데이터베이스와 컬렉션을 생성하는 코드입니다. 수정하지 마세요!
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["cafe"]
orders = db["menu"]

# item.category를 기준으로 오름차순 정렬된 데이터를 모두 출력하세요.
for doc in orders.find().sort("item.category", 1):
    print(doc)