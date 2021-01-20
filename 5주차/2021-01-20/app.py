# 앞서 진행한 1~4를 통해 토큰을 포함한 로그인 기능을 완성해봅시다.
from flask import Flask, request, jsonify, url_for, render_template, flash, redirect, make_response
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)
from datetime import timedelta, datetime
from flask_sqlalchemy import SQLAlchemy

# JWT 구현방식 1. 웹스토리지에 담아두었다가 HTTP 헤더 값에 넣어서 요청하기 / 2. httpOnly 속성이 활성화 된 쿠키에 담아서 authorication이 필요할때마다 토큰 인증하기
# 이전 JWT 실습에서는 ajax서버를 통해 헤더값으로 날려주고 이를 통해 토큰 유효성을 체크해주고 있으므로 1번 방식인듯하다.
# 이를 응용해서 이번에는 쿠키방식으로 구현해보고자 한다.

app = Flask(__name__)
app.config['SECRET_KEY'] = "SeCrEtKeYfORAuTheNtIcAtIoN"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/profile'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
#ACCESS_TOKEN_EXPIRE_MINUTES = 15
jwt = JWTManager(app)
db = SQLAlchemy(app)

# Model 생성 후 Create
from user import User
db.create_all()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/profile')
@jwt_required
def profile():
    email = get_jwt_identity()
    print("email")
    return render_template("profile.html", email=email)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            flash("Unvalid Id or Password")
            return redirect(url_for('login'))

        # 토큰 생성 
        #access_token_expire = timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        print(user.username, user.email)
        # Set the JMT cookies in the reponse
        res = make_response(render_template('index.html', login=True, username=user.username))
        set_access_cookies(res, access_token)
        set_refresh_cookies(res, refresh_token)
        return res
    else:
        return render_template("login.html")

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        
        if email == '' or username == '' or password == '':
            flash("Unvalid values are in email or password or username")
            return redirect(url_for('signup'))
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Your Account is already registered")
            return redirect(url_for('signup'))
        
        new_user = User(email=email, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template("signup.html")

@app.route('/logout', methods=['POST'])
def logout():
    # 캐시의 토큰을 삭제
    # res = jsonify({'login': False})
    # unset_jwt_cookies(res)
    res = make_response(redirect(url_for('index')))
    unset_jwt_cookies(res)
    return res

if __name__ == '__main__':
    print(__name__)
    app.run(debug=True)