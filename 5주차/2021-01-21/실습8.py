import pymongo


# 데이터베이스와 컬렉션을 생성하는 코드입니다. 수정하지 마세요!
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["library"]
col = db["books"]

# 잘못 입력된 책 작가를 수정하기 위한 딕셔너리를 만드세요.
dt = {"title": {"$regex": "^Harry Potter"}}


# 잘못 입력된 책 작가를 수정하세요.
update_book = {"$set": {"author": "Joanne Kathleen Rowling"}}

update = col.update_many(dt, update_book)
# 몇 권의 책이 수정되었는지 확인하세요.
print(update.modified_count)

# 책이 잘 수정되었는지 확인하는 코드입니다. 수정하지 마세요!
for x in col.find():
    print(x)
