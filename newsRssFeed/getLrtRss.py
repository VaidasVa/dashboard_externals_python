import feedparser
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

ignoreList = ["Sportas", "Новини", "Wiadomości"]


def get_news():
    url = "https://www.lrt.lt/?rss"
    feed = feedparser.parse(url)
    response = list()

    if feed.status == 200:
        for entry in feed.entries:
            if entry.category not in ignoreList:
                response_item = {"title": entry.title, "category": entry.category, "url": entry.link}
                response.append(response_item)
    else:
        return "Error getting RSS feed from LRT"

    return response

