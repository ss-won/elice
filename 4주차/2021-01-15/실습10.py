
import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    res = []
    ul = soup.find("ul", class_="list_news")
    for span in ul.find_all("span", class_="tit"):
        res.append(span.get_text())
    return res


def main():
    answer = []
    url = "https://sports.donga.com/ent"

    for i in range(0, 5):
        # requests.get 메소드를 호출해보세요.
        req = requests.get(url, params={'p': 20*i+1})
        soup = BeautifulSoup(req.text, "html.parser")

        answer += crawling(soup)

    # crawling 함수의 결과를 출력합니다.
    print(answer)


if __name__ == "__main__":
    main()
