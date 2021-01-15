import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # 기사에서 내용을 추출하고 반환하세요.
    div = soup.find("div", id="articleBodyContents")
    str1 = "// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}"
    return div.get_text().replace("\n", "").replace("\t", "").replace(str1, "")


def get_href(soup):
    # 각 분야별 속보 기사에 접근할 수 있는 href를 리스트로 반환하세요.
    res = []
    ul = soup.find("ul", "type06_headline")
    for a in ul.find_all("a", "nclicks(fls.list)"):
        res.append(a["href"])
    return res


def get_request(section):
    # 입력된 분야에 맞는 request 객체를 반환하세요.
    # 아래 url에 쿼리를 적용한 것을 반환합니다.
    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    url = "https://news.naver.com/main/list.nhn"

    sections = {"정치": 100, "경제": 101, "사회": 102,
                "생활": 103, "세계": 104, "과학": 105}
    req = requests.get(url, headers=custom_header,
                       params={"sid1": sections[section]})  # params 매개변수를 올바르게 설정하세요.
    return req


def main():
    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    list_href = []
    result = []

    # 섹션을 입력하세요.
    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n  > ')

    req = get_request(section)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)

    for href in list_href:
        href_req = requests.get(href, headers=custom_header)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result.append(crawling(href_soup))
    print(result)


if __name__ == "__main__":
    main()
