import requests
from bs4 import BeautifulSoup
from wc import create_word_cloud
import string


def crawling(soup):
    # 기사에서 내용을 추출하고 반환하세요.
    div = soup.find('div', class_="_article_body_contents")

    result = div.get_text().replace('\n', '').replace(
        '// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}', '').replace('\t', '')

    for p in string.punctuation:
        result.replace(p, "")
    return result


def main():
    custom_header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=421&aid=0004611563"
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    text = crawling(soup)
    create_word_cloud(text)


if __name__ == "__main__":
    main()
