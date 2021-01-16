import requests
from bs4 import BeautifulSoup


def getCapitals():
    countryAndCapitals = {}

    url = "https://ko.wikipedia.org/wiki/나라_이름순_수도_목록"

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    content = soup.find("div", class_="mw-content-ltr")
    uls = content.find_all("ul")[1:15]

    for ul in uls:
        for li in ul.find_all("li"):
            result = []
            for a in li.find_all("a"):
                if a.has_attr("title"):
                    result.append(a.get_text())

            if result != []:
                country = result[0]
                capital = result[1:]

                countryAndCapitals[country] = capital
    return countryAndCapitals
