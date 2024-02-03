import feedparser


class CryptoNews:
    """
    Gets Crypto news titles from:
        - https://www.coindesk.com/
        - https://www.newsbtc.com/
    """
    COIN_DESK_RSS_URL = 'https://www.coindesk.com/arc/outboundfeeds/rss/'
    NEWS_BTC_RRS_URL = 'https://www.newsbtc.com/feed/'

    def __init__(self):
        self.coin_desk_feed = feedparser.parse(self.COIN_DESK_RSS_URL)
        self.news_btc_feed = feedparser.parse(self.NEWS_BTC_RRS_URL)

    def get_titles(self, no_of_titles=10) -> list:
        """
        Gets last titles from sites about cryptocurrencies
        :param no_of_titles: amount of titles (10 per site is default)
        :return: list of titles (20 by default)
        """
        titles = []
        for entry in self.coin_desk_feed.entries[:no_of_titles]:
            titles.append(entry.title)
        for entry in self.news_btc_feed.entries[:no_of_titles]:
            titles.append(entry.title)
        return titles
