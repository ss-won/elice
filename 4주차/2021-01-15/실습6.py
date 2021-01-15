import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    result = []
    div = soup.find("div", class_="list_issue")
    for a in div.find_all("a"):
        result.append(a.get_text())
    return result


def main():
    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    url = "http://www.naver.com"
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    # crawling 함수의 결과를 출력합니다.
    print(crawling(soup))


if __name__ == "__main__":
    main()
