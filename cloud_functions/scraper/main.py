import feedparser
from google.cloud import pubsub_v1
import json
from datetime import datetime


project_id = "your_project_id"
topic_id = "crypto-news-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)


class CryptoNewsFetcher:
    COIN_DESK_RSS_URL = 'https://www.coindesk.com/arc/outboundfeeds/rss/'
    NEWS_BTC_RSS_URL = 'https://www.newsbtc.com/feed/'

    def fetch_titles(self, no_of_titles=10):
        titles = []
        for url in [self.COIN_DESK_RSS_URL, self.NEWS_BTC_RSS_URL]:
            feed = feedparser.parse(url)
            titles.extend([entry.title for entry in feed.entries[:no_of_titles]])
        return titles


def publish_crypto_news(event, context):
    fetcher = CryptoNewsFetcher()
    titles = fetcher.fetch_titles(no_of_titles=10)

    for title in titles:
        message_json = json.dumps({
            "title": title,
            "timestamp": datetime.now().isoformat()
        })
        message_bytes = message_json.encode("utf-8")
        publisher.publish(topic_path, data=message_bytes)
