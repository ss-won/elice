from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

board = []


@app.route('/')
def index():
    return render_template('list.html', rows=board)


@app.route('/add', methods=['POST'])
def add():
    print(request.method)
    if request.method == 'POST':
        board.append([request.form['name'], request.form['context']])
        return redirect(url_for('index'))
    else:
        return render_template('list.html', rows=board)


@app.route('/delete/<int:uid>')
def delete(uid):
    # 1번을 해보세요!
    board.pop(uid-1)
    return redirect(url_for('index'))


@app.route('/update/<int:uid>', methods=['GET', 'POST'])
def update(uid):
    if request.method == 'POST':
        # 2번을 해보세요!
        name = request.form['name']
        context = request.form['context']
        board[uid-1] = [name, context]
        return redirect(url_for('index'))
    else:
        return render_template('update.html', index=uid, rows=board)


if __name__ == '__main__':
    app.run(debug=True)
