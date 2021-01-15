import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    # 각각의 href 페이지에 들어있는 기사 내용을 반환합니다.
    div = soup.find("div", "text_area")
    return div.get_text().replace("\n", "").replace("\t", "")


def get_href(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    # 상위 페이지에서의 href를 찾아 리스트로 반환합니다.
    res = []
    div = soup.find("div", "w_news_list")
    for a in div.find_all("a", "news"):
        res.append("https://news.sbs.co.kr"+a["href"])
    return res
    # https://news.sbs.co.kr/news/endPage.do?news_id=N1006173032


def main():
    list_href = []
    list_content = []

    url = "https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)
    print(list_href)

    for url in list_href:
        href_req = requests.get(url)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result = crawling(href_soup)
        list_content.append(result)

    print(list_content)


if __name__ == "__main__":
    main()
