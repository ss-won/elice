import pymongo
import csv

# Flask를 연동합니다.
from flask import Flask, render_template, request

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

# html 화면을 출력합니다.
@app.route("/")
def main():
    return render_template("main.html")


@app.route("/save", methods=["POST"])
def save():
    data = {
        "show_id": request.form["show_id"],
        "type": request.form["type"],
        "title": request.form["title"],
        "director": request.form["director"],
        "cast": request.form["cast"],
        "country": request.form["country"],
        "date_added": request.form["date_added"],
        "release_year": request.form["release_year"],
        "rating": request.form["rating"],
        "duration": request.form["duration"],
        "listed_in": request.form["listed_in"],
        "description": request.form["description"],
    }
    res = col.insert(data)
    return render_template("main.html")


# 데이터의 수와 목록을 확인하는 메소드를 작성하세요.
@app.route("/list")
def list_title():
    res = []
    for doc in col.find():
        res.append(doc)
    return render_template("list.html", count=len(res), title=res)
