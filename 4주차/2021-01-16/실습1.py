# 네이버 증권에서 원하는 항목의 주가를 파싱해봅시다.
import time
from random import randint
import requests
from bs4 import BeautifulSoup


def parse_stock(company_code):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.368'}
    # SAMSUNG
    url = f"https://finance.naver.com/item/main.nhn?code={company_code}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return print("Unable to access")
    soup = BeautifulSoup(response.text, 'html.parser')
    stock = soup.select_one("div > p.no_today > em.no_down > span.blind").text
    print(stock)

#     soup = BeautifulSoup(response.text, 'html.parser')
#chart_area > div.rate_info > div > p.no_today
#chart_area > div.rate_info > div > p.no_today > em

# select : 여러개 (find_all), select_one : 단일 태그 검색
# result = soup.select_one("div > p.no_today > em.no_down > span.blind").text
# print(result)

# 주식 종목코드 확인 방법!
# https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage


company_list = ['005380', '005930', '066570']

start = time.time()
PERIOD_OF_TIME = 5
while True:
    time.sleep(randint(1, 2))

    for company in company_list:
        parse_stock(company)
    print("------------------------")
    if time.time() > start + PERIOD_OF_TIME:
        break

print("Done!")


# # 네이버 증권에서 원하는 항목의 주가를 파싱해봅시다.
# import time
# from random import randint
# import requests
# from bs4 import BeautifulSoup

# def parse_stock(company_code):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.368'}
#     url = "https://finance.naver.com/item/main.nhn?code=" + company_code

#     response = requests.get(url, headers=headers)

#     if response.state_code != 200:
#         return print("Unable to access")

#     soup = BeautifulSoup(response.text, 'html.parser')
#     # print(soup.title)
#     # print(soup.title.string)
#     # print(soup.title.parent)

#     # print(soup.find_all('div'))
#     # print(soup.find_all(id="u_skip"))
#     # print(soup.find_all(class_="no_today"))

#     # result = soup.select("div > p.no_today > em > span.blind")
#     stock = soup.select_one("div > p.no_today > em > span.blind").text
#     name = soup.select_one("#middle > div.h_company > div.wrap_company > h2 > a").text
#     print(name, stock)


# company_list = ['005380', '005930', '066570']

# start = time.time()
# PERIOD_OF_TIME = 5
# while True:
#     time.sleep(randint(1, 2))

#     for company in company_list:
#         parse_stock(company)
#     print("------------------------")
#     if time.time() > start + PERIOD_OF_TIME:
#         break

# print("Done!")


# # 주식 종목코드 확인 방법!
# # https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage
