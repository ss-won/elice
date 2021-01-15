from bs4 import BeautifulSoup

# index.html을 불러와서 BeautifulSoup 객체를 초기화해 soup에 저장하세요.
soup = BeautifulSoup(open("index.html"), "html.parser")

# soup를 사용하여 요구되는 정보를 출력해보세요.
print(soup.find("div", class_="elice").find("p").get_text())
