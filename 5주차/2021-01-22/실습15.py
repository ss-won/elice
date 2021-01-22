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

# 새로운 데이터 딕셔너리를 만들고 컬렉션에 삽입하세요.
new_movie = {
    "show_id": 95889578,
    "type": "Movie",
    "title": "Sweet Home",
    "director": "Eungbok Lee",
    "cast": "Gang Song",
    "country": "Korea",
    "date_added": "18-Dec-20",
    "release_year": "2020",
    "rating": "TV-MA",
    "duration": "497min",
    "listed_in": "Thrillers",
    "description": "A teenage boy shutting off the world and stuck in a room. Hyunsoo comes out of the world. Humans turned into monsters. You still have to live. I'm still a person. You have to fight with your neighbors.",
}

# 데이터를 삽입한 결과를 저장하세요.
new_add_data = col.insert_one(new_movie)

# 삽입된 데이터를 확인하기 위한 코드입니다. 수정하지 마세요!
print(col.find_one(new_add_data.inserted_id))

for doc in col.find().sort("title", 1):
    print(doc["title"])