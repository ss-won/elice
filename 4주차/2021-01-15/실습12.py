import requests
from bs4 import BeautifulSoup


def get_href(soup):
    # 각 기사에 접근할 수 있는 href를 리스트로 반환하세요.
    res = []
    div = soup.find("div", "postSubjectContent")
    for a in div.find_all("a", 'lt1'):
        res.append("https:"+a["href"])
    return res


def main():
    list_href = []

    # href 수집할 사이트 주소 입력
    url = "https://news.nate.com/recent?mid=n0100"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)

    print(list_href)


if __name__ == "__main__":
    main()
