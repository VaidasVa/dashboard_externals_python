from flask import Blueprint

from newsRssFeed import getLrtRss

news_bp = Blueprint('news_bp', __name__)


@news_bp.route('/api/v1/news', methods=['GET'])
def get_news():
    response = getLrtRss.get_news()
    print("News received")
    return response
