import pymongo

# 데이터베이스와 Collection을 생성하는 코드입니다. 수정하지 마세요!
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["library"]
col = db["books"]

# books Collection에 들어있는 책들을 출력하세요.
for find_book in col.find(
    {
        "$or": [
            {"author": "Antoine de Saint-Exupery"},
            {"author": "Ernest Miller Hemingway"},
        ]
    }
):
    print(find_book["title"])

for find_book in col.find(
    {"$and": [{"author": "Joanne Kathleen Rowling"}, {"date_received": "2017-07-21"}]}
):
    print(find_book["title"])
