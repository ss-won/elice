# csv 라이브러리를 import하세요.
import pymongo
import csv


# 데이터베이스와 컬렉션을 생성하는 코드입니다. 수정하지 마세요!
client = pymongo.MongoClient("localhost", 27017)

db = client["netflix"]
col = db["titles"]

# netflix_titles.csv을 읽기 모드로 여세요.
reader = open("netflix_titles.csv", "r")

# csv 파일의 데이터를 딕셔너리 형태로 읽으세요.
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

# 읽은 데이터를 titles 컬렉션에 삽입하세요.
col.insert_many(data)

# 목록이 잘 들어갔는지 확인하기 위한 코드입니다. 수정하지 마세요!
print(col.find_one())