import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    # 1장 실습의 영화 리뷰 추출 방식과 동일합니다.
    res = []
    ul = soup.find("ul", "rvw_list_area")
    for a in ul.find_all("strong"):
        res.append(a.get_text().replace("\n", ""))
    return res


def get_href(soup):
    # 검색 결과, 가장 위에 있는 영화로 접근할 수 있는 href를 반환하세요.
    link = "https://movie.naver.com"+soup.find("dt").find("a")["href"]
    link = link.replace("basic", "review")
    # print(link)
    return link


def get_url(movie):
    # 입력된 영화를 검색한 결과의 url을 반환하세요.
    url = f"https://movie.naver.com/movie/search/result.nhn?query={movie}&section=all&ie=utf8"
    return url


def main():
    list_href = []

    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    # 섹션을 입력하세요.
    movie = input('영화 제목을 입력하세요. \n  > ')

    url = get_url(movie)
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    movie_url = get_href(soup)

    href_req = requests.get(movie_url)
    href_soup = BeautifulSoup(href_req.text, "html.parser")

    list_href = crawling(href_soup)
    print(list_href)


if __name__ == "__main__":
    main()
