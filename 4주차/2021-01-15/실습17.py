import requests
import json  # json import하기

# custom_header을 통해 아닌 것 처럼 위장하기
custom_header = {
    'referer': 'https://www.naver.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}


def get_keyword_ranking():
    result = []
    url = "https://apis.naver.com/mobile_main/srchrank/srchrank?frm=main&ag=20s&gr=0&ma=-2&si=-2&en=-2&sp=-2"
    req = requests.get(url, headers=custom_header)

    if req.status_code == requests.codes.ok:
        print("접속 성공")
        json_data = json.loads(req.text)
        for d in json_data["data"]:
            if len(d["keyword_synonyms"]) == 0:
                result.append([d["keyword"], None])
            else:
                result.append([d["keyword"], d["keyword_synonyms"]])

    else:
        print("Error code")

    return result


def main():
    result = get_keyword_ranking()
    i = 1
    for keyword, synonyms in result:
        if synonyms:
            print(f"{i}번째 검색어 : {keyword}, 연관검색어 : {synonyms}")
        else:
            print(f"{i}번째 검색어 : {keyword}")
        i += 1


if __name__ == "__main__":
    main()
