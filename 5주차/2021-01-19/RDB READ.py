# DATABASE
from flask import Flask, render_template, request, url_for, redirect
# 1번을 해보세요!
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('database.db')
print("Opened database successfully")
conn.execute('CREATE TABLE IF NOT EXISTS Board (name TEXT, context TEXT)')
print("Table created successfully")
name = [['Elice', 15], ['Dodo', 16], ['Checher', 17], ['Queen', 18]]
for i in range(4):
    conn.execute(
        f"INSERT INTO Board(name, context) VALUES('{name[i][0]}', '{name[i][1]}')")
conn.commit()
conn.close()


@app.route('/')
def board():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("select * from Board")
    rows = cur.fetchall()
    con.close()
    print("DB:")
    for i in range(len(rows)):
        print(rows[i][0] + ':' + rows[i][1])
    return render_template('board.html', rows=rows)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        name = request.form['name']
        # 2번을 해보세요!
        con = sqlite3.connect("database.db")
        print("Opened database successfully")
        # 3번을 해보세요!
        cur = con.cursor()
        # 4번을 해보세요!
        cur.execute(f"SELECT * FROM BOARD WHERE name='{name}'")
        print("Select Query successfully executed")
        # 5번을 해보세요!
        rows = cur.fetchall()
        # 6번을 해보세요!
        con.close()
        print("DB:")
        for i in range(len(rows)):
            print(rows[i][0] + ':' + rows[i][1])
        return render_template('search.html', rows=rows)
    else:
        return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
