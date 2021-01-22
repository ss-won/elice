import pymongo
import csv


# 데이터를 삽입하는 코드입니다. 수정하지 마세요!
client = pymongo.MongoClient("localhost", 27017)

db = client["netflix"]
col = db["titles"]

reader = open("netflix_titles.csv", "r")
data = csv.DictReader(
    reader,
    (
        "show_id",
        "type",
        "title",
        "director",
        "cast",
        "country",
        "date_added",
        "release_year",
        "rating",
        "duration",
        "listed_in",
        "description",
    ),
)

result = col.insert_many(data)

# 오름차순 정렬된 작품 전체 제목을 출력하세요.
for d in col.find().sort("title", 1):
    print(d["title"])
