import pymongo


# 데이터베이스와 컬렉션을 생성하는 코드입니다. 수정하지 마세요!
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["cafe"]
orders = db["menu"]

# 3개의 데이터를 생략하고 출력하세요.
for doc in orders.find().skip(3):
    print(doc)