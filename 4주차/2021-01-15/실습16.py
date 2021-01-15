import requests
import json

custom_header = {
    'referer': 'http://http://finance.daum.net/quotes/A048410#home',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}


def get_data():
    result = []
    # 상위 10개 기업의 정보를 얻는 API url을 작성하세요.
    url = "http://finance.daum.net/api/search/ranks?limit=10"
    req = requests.get(url, headers=custom_header)

    if req.status_code == requests.codes.ok:
        print("접속 성공")
        # API에 접속에 성공하였을 때의 logic을 작성해주세요.
        # JSON 데이터의 원하는 부분만 불러와 result에 저장해주세요.
        stock_data = json.loads(req.text)
        for d in stock_data["data"]:
            result.append((d['rank'], d['name'], d['tradePrice']))
    else:
        print("접속 실패")

    return result


def main():
    data = get_data()

    for d in data:
        print(d)


if __name__ == "__main__":
    main()
