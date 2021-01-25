from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def parse_stock_price(stock_code):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.368'}
    url = "https://finance.naver.com/item/main.nhn?code=" + str(stock_code)
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Unable to parse: ", response.status_code)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    price = soup.select_one(
        "#chart_area > div.rate_info > div > p.no_today > em > span.blind").text

    print(stock_code, " : ", price)

    return price


@app.route('/')
def home():
    return render_template('index3.html')


@app.route('/stock', methods=['POST'])
def get_stock():
    stockCode = request.form["stockCode"]
    price = parse_stock_price(stockCode)
    if price != None:
        return jsonify({"result": "success", "price": price})
    else:
        return jsonify({"result": "failed", "msg": "해당 종목이 없습니다."})


if __name__ == '__main__':
    app.run(debug=True)
