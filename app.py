from flask import Flask, render_template, request
from authenticity import check_news_auth
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/check_news', methods=['POST'])
def check_news():
    news = request.form['txtSearch'].strip()
    if not news:
        msg = "Ensure you enter a description to be checked!"
    elif len(news) < 30:
        msg = "Please input a larger paragraph to ensure the prediction is accurate"
    else:
        try:
            msg = check_news_auth(news)
        except Exception as err:
            msg = str(err)
    return msg


if __name__ == '__main__':
    app.run()
