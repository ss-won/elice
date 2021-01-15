from bs4 import BeautifulSoup
import requests
import json  # json import하기

custom_header = {
    'referer': 'https://www.mangoplate.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}


def get_restaurants(name):
    # 검색어 name이 들어왔을 때 검색 결과로 나타나는 식당들을 리스트에 담아 반환하세요.
    restaurant_list = []
    url = f"https://www.mangoplate.com/search/{name}"
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    restaurants = soup.find_all("div", "list-restaurant-item")
    for rest in restaurants:
        info = rest.find("div", "info")
        href = info.find("a")["href"]
        title = info.find("h2").get_text().replace("\n", "").replace(" ", "")
        restaurant_list.append([title, href])
    return restaurant_list


def main():
    name = input()

    restaurant_list = get_restaurants(name)

    print(restaurant_list)


if __name__ == "__main__":
    main()
