from utils import User, Post


class Reaction:
    # 아래 코드의 빈 부분을 완성합니다.
    def __init__(self, reaction_type, post, user):
        if reaction_type not in ("LIKE", "LOVE", "HAHA", "SAD", "ANGRY", "WOW"):
            raise ValueError("Invalid reaction_type")
        if not isinstance(post, Post):
            raise TypeError("Invalid post type")
        if not isinstance(user, User):
            raise TypeError("Invalid user type")

        self.reaction_type = reaction_type
        self.post = post
        self.user = user
        post.reactions.append(self)

# 아래 코드의 빈 부분을 완성합니다.


class Like(Reaction):
    def __init__(self, post, user):
        super().__init__("LIKE", post, user)
        post.positive_reactions += 1


class Angry(Reaction):
    # 아래 코드의 빈 부분을 완성합니다.
    def __init__(self, post, user):
        super().__init__("ANGRY", post, user)
        post.negative_reactions += 1
