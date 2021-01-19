# 1번을 해보세요!
from main import db
# 2번을 해보세요!


class Member(db.Model):
    # 3번을 해보세요!
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    # 4번을 해보세요!

    def __init__(self, name, age):
        self.name = name
        self.age = age
