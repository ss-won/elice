from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

names = ['John', 'Jane', "Elice"]


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/user', methods=["GET", "POST", "DELETE"])
def user():
    if request.method == "POST":
        username = request.form["username"]
        if username not in names:
            names.append(username)
        return redirect(url_for('user'))
    elif request.method == "DELETE":
        username = request.form["username"]
        #print(username)
        if username in names:
            names.remove(username)
            return jsonify(result="success")
        else:
            return jsonify(result="falid", err="사용자가 존재하지 않습니다.")
    return render_template("user.html", names=names)


if __name__ == '__main__':
    app.run(debug=True)

# REST API : 
# REST 원칙으로 구현한 API로, 해당 요청 함수에 의해 자원들의 정보를 제공하며 이를 구분하는 URI를 나타낸다.
# URI에 자원을 표현하는 명사로 표기, METHOD에는 HTTP 행위를 동사로 표기한다.
# 공용 규약이 따로 없기 때문에 회바회 팀바팀으로 달라질 수 있다.