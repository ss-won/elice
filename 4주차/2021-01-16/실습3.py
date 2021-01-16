# 망고플레이트에서 맛집을 찾아 봅시다.
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.368'}
url = "https://www.mangoplate.com/search/2021%EB%A7%9D%EA%B3%A0%ED%94%8C%EB%A0%88%EC%9D%B4%ED%8A%B8%EC%9D%B8%EA%B8%B0%EB%A7%9B%EC%A7%91"

res_info = {}
# 1. url에서 나온 음식점 목록 조회
req = requests.get(url, headers=headers).text
soup = BeautifulSoup(req, "html.parser")
div = soup.find_all("div", "list-restaurant-item")
for d in div:
    tit = d.find("h2", "title").text.replace(" ", "").replace("\n", "")
    res_info[tit] = {'roadAddress': '', 'Address': '', 'tel': '', 'time': ''}
    # print(tit)
# 2. 음식점의 주소, 전화번호, 영업시간 조회
for d in div:
    href = d.find("a")["href"]
    rq = requests.get(
        f"https://www.mangoplate.com{href}", headers=headers).text
    inner_soup = BeautifulSoup(rq, "html.parser")
    # key 가져오기
    name, branch = inner_soup.find(
        'h1', 'restaurant_name').text, inner_soup.find('p', 'branch').text
    if not branch == '':
        rname = f"{name}({branch})"
    else:
        rname = name
    table = inner_soup.find("table", "info")
    for tr in table.find_all("tr"):
        if '주소' in tr.text:
            adr = tr.text.strip().split("\n")
            res_info[rname]['roadAddress'] = adr[1]
            res_info[rname]['Address'] = adr[3]
        elif '전화번호' in tr.text:
            res_info[rname]['tel'] = tr.text.strip().split("\n")[-1]
        elif '영업시간' in tr.text:
            res_info[rname]['time'] = tr.text.strip().split("\n")[-1]
            # print(tr.text.strip().split("\n")[-1])

for res, info in res_info.items():
    print("\n")
    print(res, info['roadAddress'], info['Address'],
          info['tel'], info['time'], sep="\n")
