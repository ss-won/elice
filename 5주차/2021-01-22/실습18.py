import pymongo
import csv

# Flask를 연동합니다.
from flask import Flask, render_template

app = Flask(__name__)

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

# main.html을 반환하는 메소드를 작성하세요.
@app.route("/")
def main():
    return render_template("main.html")