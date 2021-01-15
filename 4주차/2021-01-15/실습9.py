import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    res = []
    ul = soup.find("ul", class_="rvw_list_area")
    for li in ul.find_all("li"):
        res.append(li.find("strong").get_text())
    return res


def main():
    custom_header = {
        'referer': 'https://movie.naver.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    url = "https://movie.naver.com/movie/bi/mi/review.nhn?code=168058#"
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    # crawling 함수의 결과를 출력합니다.
    print(crawling(soup))


if __name__ == "__main__":
    main()
