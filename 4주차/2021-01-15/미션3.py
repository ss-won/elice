from bs4 import BeautifulSoup
import requests
import json  # json import하기

custom_header = {
    'referer': 'https://www.mangoplate.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}


def get_reviews(code):
    comments = []

    url = f"https://stage.mangoplate.com/api/v5{code}/reviews.json?language=kor&device_uuid=V3QHS15862342340433605ldDed&device_type=web&start_index=0&request_count=5&sort_by=2"
    req = requests.get(url, headers=custom_header)

    # req에 데이터를 불러온 결과가 저장되어 있습니다.
    # JSON으로 저장된 데이터에서 댓글을 추출하여 comments에 저장하고 반환하세요.
    if req.status_code == requests.codes.ok:
        print("접속 성공")
        json_data = json.loads(req.text)
        for d in json_data:
            comment = d["comment"]
            rvw = comment["comment"].replace("\n", "")
            comments.append(rvw)
    else:
        print("Error")
    return comments


def get_restaurants(name):
    url = f"https://www.mangoplate.com/search/{name}"
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    # soup에는 특정 키워드로 검색한 결과의 HTML이 담겨 있습니다.
    # 특정 키워드와 관련된 음식점의 이름과 href를 튜플로 저장하고,
    # 이름과 href를 담은 튜플들이 담긴 리스트를 반환하세요.
    res = []
    div = soup.find_all("div", "list-restaurant-item")
    for d in div:
        restaurant = d.find("div", "info")
        link = restaurant.find("a")["href"]
        title = restaurant.find("h2", "title").get_text()
        res.append([title, link])
    return res


def main():
    name = input("검색어를 입력하세요 : ")

    restuarant_list = get_restaurants(name)

    for r in restuarant_list:
        print(r[0])
        print(get_reviews(r[1]))
        print("="*30)
        print("\n"*2)


if __name__ == "__main__":
    main()
