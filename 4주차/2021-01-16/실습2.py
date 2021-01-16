# 다음 뉴스 헤드라인을 파싱해봅시다 :)
import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.368'}
url = "https://news.daum.net/ranking/popular/entertain"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
ul = soup.find("ul", "list_news2")
for a in ul.find_all("a", "link_txt"):
    print(a.text)
