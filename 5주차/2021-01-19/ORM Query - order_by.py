from models import Member
from flask import Flask, request, render_template, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app, db)


@app.route('/list')
def _list():
    # 1번을 해보세요!
    member_list = Member.query.order_by(Member.age)
    return render_template('member_list.html', member_list=member_list)


@app.route('/', methods=['GET', 'POST'])
def _add():
    if(Member.query.count() == 0):
        file = open("randomname.txt", 'r')
        for i in file.readlines():
            a, b = i.split()
            member = Member(a, int(b))
            db.session.add(member)
        db.session.commit()
        file.close()
    if request.method == 'POST':
        name = request.form['name']
        try:
            age = int(request.form['age'])
        except:
            return "나이는 숫자만 입력하세요."
        member = Member(name, age)
        db.session.add(member)
        db.session.commit()
        return redirect(url_for('_list'))
    elif request.method == 'GET':
        return render_template('add.html')


if __name__ == "__main__":
    app.run()
