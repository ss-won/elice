from bs4 import BeautifulSoup

# index.html을 불러와서 BeautifulSoup 객체를 초기화해 soup에 저장하세요.
soup = BeautifulSoup(open("index.html"), "html.parser")
print(soup)

# index.html이 같은 폴더 내에 있다고 가정한다.
