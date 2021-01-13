class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.shared_users = []
        self.is_private = False

    def share(self, user):
        self.shared_users.append(user)


class PrivatePost(Post):
    # 생성자를 구현합니다.
    # is_private 속성을 True 로 설정합니다.
    # 생성자 오버라이딩
    def __init__(self, author, content):
        super().__init__(author, content)
        self.is_private = True

    # share 메소드를 호출 시 TypeError를 발생시킵니다.
    # 메소드 오버라이딩
    def share(self, user):
        raise TypeError("비밀 포스트는 공유하실 수 없습니다.")
