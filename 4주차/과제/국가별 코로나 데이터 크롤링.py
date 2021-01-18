import requests
import re
from bs4 import BeautifulSoup
# 제출 버튼을 눌러야만 채점 및 점수 부여가 됩니다.

headers = headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "https://www.worldometers.info/coronavirus/"

# request 요청


def get_request():
    soup = None
    try:
        req = requests.get(url, headers=headers)
        if req.status_code != 200:
            print("http request에 실패하였습니다.")
        else:
            # 1. url html을 담고 있는 soup 객체 생성하기
            soup = BeautifulSoup(req.text, "html.parser")
    except:
        print("Unhandled Error")
    return soup

# crawling 함수


def crawling(soup):
    corona_info = {}

    # 2. soup 객체에 있는 국가들의 코로나 관련 데이터 크롤링하기
    tbody = soup.find("tbody")
    trs = tbody.find_all("tr")
    continents = tbody.find_all("tr", "row_continent")
    trs = [tr for tr in trs if tr not in continents]

    for tr in trs:
        tds = tr.find_all("td")
        # 1(국가이름), 2(총 확진자), 4(총 사망자), 6(총 완치자)
        tmp = [tds[i].text.replace("\n", "").replace(",", "").replace(
            " ", "") for i in range(len(tds)) if i in [1, 2, 4, 6]]
        arr = [x for x in tmp[1:]]
        # values값은 int지만, 유효하지 않은 값일 경우 ""N\A" 출력
        t_case, t_death, t_recover = map(lambda x: int(
            x) if x != '' and x != 'N/A' else 'N/A', arr)
        corona_info[tmp[0]] = {'확진자': t_case, '사망자': t_death, '완치': t_recover}

    return corona_info


if __name__ == "__main__":
    soup = get_request()
    if soup != None:
        res = crawling(soup)
        # 3. 크롤링한 결과를 형식에 맞게 출력하기
        for key, value in res.items():
            print(key, value)
    else:
        print("failed: get_request()")
