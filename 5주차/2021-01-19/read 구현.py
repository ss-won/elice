from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)

board = []


@app.route('/')
def index():
    return render_template('Board.html', rows=board)


@app.route('/create', methods=['POST'])
def create():
    board.append([request.form['name'], request.form['context']])

    return json.dumps({"status": 200, "result": {"id": len(board)}})


@app.route('/read', methods=['GET'])
def read():
    # 1번을 해보세요.
    return json.dumps({"status": 200, "result": board})


if __name__ == '__main__':
    app.run(debug=True)
