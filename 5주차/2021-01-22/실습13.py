# pymongo 라이브러리를 이용해 파이썬과 MongoDB를 연결하세요.
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

# netflix 데이터베이스를 생성하세요.
db = client["netflix"]

# titles 컬렉션을 생성하세요.
col = db["titles"]

col.insert_one({"title": "Sweet Home"})
# 데이터베이스와 컬렉션 목록을 reuslt 변수에 저장하세요.


result1 = client.list_database_names()
result2 = db.list_collection_names()

# 목록이 잘 들어갔는지 확인하기 위한 코드입니다. 수정하지 마세요!
print(result1)
print(result2)