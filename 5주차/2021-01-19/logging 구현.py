from flask import Flask, render_template

app = Flask(__name__)


# 1번을 해보세요!
@app.errorhandler(404)
# 2번을 해보세요!
def page_not_found(error):
    # 3번을 해보세요!
    app.logger.error(error)
    # 4번을 해보세요!
    return render_template('page_not_found.html')


@app.route('/')
def hello_elice():
    return "Hello Elice!"


if __name__ == '__main__':
    app.run()
