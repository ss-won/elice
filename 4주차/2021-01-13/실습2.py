from user import User


class Post:

    # 생성자는 매개변수로 작성자와 내용을 받아,
    # 그 값을 속성에 저장합니다.
    def __init__(self, author, content):

        # 속성들을 초기화합니다.
        self.author = author
        self.content = content

        # 아래의 코드를 수정하세요.
        self.likes = []

    # num_likes 메소드를 생성합니다.
    # 아래의 코드를 수정해서 메소드를 완성하세요.
    def num_likes(self):
        return len(self.likes)

    # likes 메소드를 생성합니다.
    # 아래의 코드를 수정해서 메소드를 완성하세요.
    def like(self, user):
        if not user in self.likes:
            self.likes.append(user)


# 새로운 사용자 me를 생성합니다.
me = User("Elice")

# 인스턴스 = 클래스라는 틀을 통해 만들어 낸 객체
# 아래에 자유롭게 인스턴스를 생성하고 테스트해 보세요.
my_post = Post(me, "I luv racoon🦝")
print(my_post.content)

print(my_post.num_likes())
my_post.like(me)
print(my_post.num_likes())
