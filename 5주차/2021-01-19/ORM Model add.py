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
    member_list = Member.query.all()
    return render_template('member_list.html', member_list=member_list)

# 1번을 해보세요!


@app.route('/', methods=['GET', 'POST'])
def _add():

    # 2번을 해보세요!
    if request.method == 'POST':
        name = request.form['name']
        # 3번을 해보세요!
        try:
            age = int(request.form['age'])
        except:
            return "나이는 숫자만 입력하세요"
        member = Member(name, age)
        db.session.add(member)
        db.session.commit()
        # 4번을 해보세요!
        return redirect(url_for('_list'))
    else:
        return render_template('add.html')


if __name__ == "__main__":
    app.run()
