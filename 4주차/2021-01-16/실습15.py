import requests
from bs4 import BeautifulSoup
from wc import create_word_cloud


def crawling(soup):
    # 기사에서 내용을 추출하고 반환하세요.
    div = soup.find('div', class_="_article_body_contents")

    result = div.get_text().replace('\n', '').replace(
        '// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}', '').replace('\t', '')

    return result


def get_href(soup):
    result = []

    cluster_body = soup.find("div", class_="cluster_body")

    for cluster_text in cluster_body.find_all("div", class_="cluster_text"):
        result.append(cluster_text.find("a")["href"])

    return result


def get_request(section, custom_header):
    url = "https://news.naver.com/main/main.nhn"
    section_dict = {"정치": 100,
                    "경제": 101,
                    "사회": 102,
                    "생활": 103,
                    "세계": 104,
                    "과학": 105}
    return requests.get(url, params={"sid1": section_dict[section]}, headers=custom_header)


def main():
    custom_header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    list_href = []
    result = []

    # 섹션을 입력하세요.
    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n  > ')

    req = get_request(section, custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)

    for href in list_href:
        href_req = requests.get(href, headers=custom_header)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result.append(crawling(href_soup))

    text = " ".join(result)
    create_word_cloud(text)


if __name__ == "__main__":
    main()
