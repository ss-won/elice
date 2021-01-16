import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    contents = soup.find("div", id="articleBodyContents").get_text().replace("\n", "").replace(
        "// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}", "").replace(" ", "").replace("\t", "").replace("▶", "")
    return contents


def main():
    custom_header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=001&aid=0011575988"
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    print(crawling(soup))


if __name__ == "__main__":
    main()
