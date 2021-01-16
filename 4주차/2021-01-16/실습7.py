import requests
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
API_KEY = os.getenv('API_KEY')
# 4. TODO: {강남구: 100, 용산구: 80, 서초구: 90, 마포구: 60}
# 각 지역별, 평균 공시지가를 구해서 Dictionary 형태로 저장하기!


def avgJiga(rows):
    total = 0
    for row in rows:
        total += int(row['JIGA'])
    return total / len(rows)


def get_data(targets):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.368'}
    for target in targets:
        url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/IndividuallyPostedLandPriceService/1/100/{target}/%20/%20/%20/%20/2020"
        # 1. JSON으로 데이터 받아오기, # 3. 100개 읽어오기
        res = requests.get(url, headers=headers)
        data = res.json()
        rows = data["IndividuallyPostedLandPriceService"]["row"]
        print(f"{target}의 평균 공시지가: {avgJiga(rows)}")


# 2. 강남구, 용산구, 서초구, 마포구 데이터 조회
regions = ['강남구', '용산구', '서초구', '마포구']
get_data(regions)
