from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["elice"]
col = db["memo"]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST', 'GET'])
def post_memo():
    if request.method == "POST":
        # 0. 사용자가 보낸 데이터를 변수에 답아봅시다!
        title_give = request.form["title_give"]
        memo_give = request.form["memo_give"]
        print(title_give, memo_give)
        # 1. db에 넣을 딕셔너리를 하나 만들어보아요.
        memo = {"title": title_give, "memo": memo_give}
        print(memo)
        # 2. 위에서 정의한 db에 Create를 해봅시다.
        data = col.insert(memo)
        #print(f"input data: {data}")
        # 3. db에 데이터를 넣었으면 성공메시지를 보내줍시다!
        return jsonify({'result': 'success'})
    # 1. db에 저장된 데이터를 가져옵시다.
    # res = []
    # for data in col.find({}):
    #     res.append({"title":data["title"], "memo":data["memo"]})
    res = list(col.find({}, {'_id': False}))
    # 2. 가져온 데이터를 jsonify를 통해 다시 보내줍시다!
    return jsonify({'result': 'success', 'memos': res})

#@app.route('/memo', methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True)
