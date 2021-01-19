from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

board = [{"id": 1, "name": "elice", "context": "test"}]


@app.route('/')
def index():
    return render_template('index.html', rows=board)


@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    board.append(data)
    return jsonify(result="success", result2=data)


@app.route('/delete', methods=['POST'])
def delete():
    # 1번을 하세요.
    if len(board) > 0:
        board.pop()
    return jsonify(result="success")


@app.route('/put', methods=['POST'])
def put():
    # 2번을 하세요.
    data = request.get_json()
    if len(board) > 0:
        board[-1] = data
    return jsonify(result="success", result2=data)
