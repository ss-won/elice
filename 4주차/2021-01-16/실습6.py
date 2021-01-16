import os
import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)
API_KEY = os.getenv('API_KEY')
data_dict = {}


def parse_result(target, data):
    rows = data['Corona19Status']['row']
    for row in rows:
        if row[target] in data_dict:
            data_dict[row[target]] += 1
        else:
            data_dict[row[target]] = 1
    return data_dict


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.368'}
i = 1
while True:
    url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/Corona19Status/{i}/{i+999}/"
    response = requests.get(url, headers=headers)
    data = response.json()
    # print(data['Corona19Status']['row'])
    if 'Corona19Status' not in data:
        break
    i += 1000
    targets = ['CORONA19_DATE', 'CORONA19_AREA', 'CORONA19_LEAVE_STATUS']
    for target in targets:
        print(parse_result(target, data))

# coronaChart = {'date':{}, 'region':{}}
# for d in data['Corona19Status']['row']:
#     if d['CORONA19_DATE'] in coronaChart['date']:
#         coronaChart['date'][d['CORONA19_DATE']] += 1
#     else:
#         coronaChart['date'][d['CORONA19_DATE']] = 1
#     if d['CORONA19_AREA'] in coronaChart['region']:
#         coronaChart['region'][d['CORONA19_AREA']] += 1
#     else:
#         coronaChart['region'][d['CORONA19_AREA']] = 1

# for val in coronaChart.values():
#     for k, v in val.items():
#         print(f"{k}: {v}")
# 1. 날짜별 확진자
# 2. 지역별 확진자
