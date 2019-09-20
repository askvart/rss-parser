import feedparser
from flask import Flask
from flask import render_template
from flask import request



app = Flask(__name__)

# Ленты RSS из интернета
RSS_FEEDS = {'avto': 'https://news.yandex.ru/auto.rss',
             'nedviga':'https://news.yandex.ru/realty.rss',
             'theatr': 'https://news.yandex.ru/theaters.rss',
             'lenta':'https://lenta.ru/rss/top7',
             'fin': 'http://www.finmarket.ru/rss/mainnews.asp',
             'vc':'http://siliconrus.com/feed/',
             'xbt': 'http://ixbt.com/export/news.rss'}


@app.route('/')
@app.route('/<publication>')
def get_news(publication='lenta'):
    ''' Функция парсит rss и рендерит шаблон'''
    query = request.args.get('publication')
    if not query or query.lower() not in RSS_FEEDS:
        publication = 'lenta'
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template('home.html',
                           articles=feed['entries'])



if __name__ == '__main__':
    app.run(port=5000, debug=True)
