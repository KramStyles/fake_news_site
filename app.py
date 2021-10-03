from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/check_news')
def check_news():
    news = request.form['txtSearch']
    return news

if __name__ == '__main__':
    app.run()
