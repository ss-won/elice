import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"

# url 변수에 담긴 url의 html 문서를 불러와 출력해보세요.
req = requests.get(url)
print(req.text)
