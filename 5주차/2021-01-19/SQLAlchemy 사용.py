from models import Member
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import json
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


@app.route('/', methods=['GET', 'POST'])
def _add():
    if request.method == 'POST':
        name = request.form['name']
        try:
            age = int(request.form['age'])
        except:
            return "나이는 숫자만 입력하세요."
        member = Member(name, age)
        db.session.add(member)
        db.session.commit()

        # 1번을 해보세요.
        m_dict, j = {}, 0
        for i in Member.query.all():
            m_dict[j] = i.name
            j += 1
        m_dict = json.dumps(m_dict)
        # 2번을 해보세요
        return jsonify(result=m_dict, status=200)
    else:
        return render_template('add.html')


if __name__ == "__main__":
    app.run()
