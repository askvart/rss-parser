from flask import Flask
from flask import render_template
import feedparser

app = Flask(__name__)

RSS_FEEDS = {'avto': 'https://news.yandex.ru/auto.rss',
             'nedviga':'https://news.yandex.ru/realty.rss',
             'theatr': 'https://news.yandex.ru/theaters.rss',
             'lenta':'https://lenta.ru/rss/top7',
             'fin': 'https://news.yandex.ru/finances.rss'}


@app.route('/')
@app.route('/<publication>')
def get_news(publication='lenta'):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template('home.html', articles=feed['entries'])



if __name__ == '__main__':
    app.run(port=5000, debug=True)
