from utils import go_to


class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content


# 아래에 LinkPost를 선언합니다.
class LinkPost(Post):
    def __init__(self, author, content, url):
        super().__init__(author, content)
        if not (url.startswith("https://") or url.startswith("http://")):
            raise ValueError("Invalid URL")
        self.url = url

    def on_click(self):
        go_to(self.url)


post = LinkPost("elice", "Hello, world!", "https://elice/io")
print(post.url, post.on_click())
