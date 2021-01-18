import requests
import re
from bs4 import BeautifulSoup

# 제출 버튼을 눌러야만 채점 및 점수 부여가 됩니다.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "https://finance.naver.com/sise/sise_group_detail.nhn?type=upjong&no=235"

def crawling(soup):
    stock, data = [], {}
    
    # 1. stock 리스트에 종목명, 현재가, 전일비, 등락률을 담아 출력하기
    tbody = soup.find("tbody")
    trs = tbody.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) >= 4: # 빈 tr은 탐색하지 않음
            tmp = [tds[i].text.replace("\n","").replace("*", "").replace("\t", "") for i in range(4)]
            # 2. 등락률이 +인 종목의 종목명, 현재가로 dict형 data를 만들기
            if tmp[3][0] == '+': # tmp[3]: 등락률, 등락률이 + 일때
                data[tmp[0]] = int(tmp[1].replace(",", "")) # tmp[0]: 종목명, tmp[1]: 현재가
            stock.append(tmp)
    
    # 3. 현재가가 오름차순이 되로록, data를 list형태로 정렬하기
    data = sorted(data.items(), key=lambda x: x[1])
    
    # 지시사항 1,2,3를 만족하는 stock, data 값 반환
    return (stock, data)
    
if __name__ == "__main__":
    # request 요청
    try:
        req = requests.get(url, headers=headers)
        if req.status_code != 200:
            print("http request에 실패하였습니다.")
        else:
            # BeautifulSoup객체로 변경
            soup = BeautifulSoup(req.text, "html.parser")
            stock, data = crawling(soup)
            print(stock, data, sep="\n\n")
    except:
        print("Unhandled Error")