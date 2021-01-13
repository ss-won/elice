from validators import validate_email


class User:

    def __init__(self, email, password, name, gender):

        # 이메일이 형식에 맞는지 확인하고, 설정합니다.
        if not validate_email(email):
            raise ValueError("invalid email")
        self.email = email

        # 비밀번호가 조건을 만족하는지 확인하고, 설정합니다.
        if len(password) < 8:
            raise ValueError("Password's length is not over 8")
        self.password = password

        # 사용자의 이름이 조건을 만족하는지 확인하고, 설정합니다.
        if name == "":
            raise ValueError("name value is none")
        self.name = name

        # 성별이 조건을 만족하는지 확인하고, 설정합니다.
        if not gender in ('M', 'F', 'O'):
            raise ValueError("invalid gender")
        self.gender = gender

        # 친구 목록을 설정합니다.
        self.friends = []

#me = User("swj960515@gmail.com", "960515", "wish", "F")
#me = User("swj960515@gmail.com", "960515jsw", "wish", "S")
#print(me.email, me.password, me.name, me.gender, me.friends)
