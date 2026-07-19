import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import requests


class NewsService:

    def __init__(self):
        self.url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/news"

    def get_news(self, limit=5):

        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()

            data = response.json()

            articles = []

            for article in data.get("articles", [])[:limit]:

                articles.append({
                    "headline": article.get("headline"),
                    "description": article.get("description"),
                    "published": article.get("published"),
                    "link": article.get("links", {}).get("web", {}).get("href")
                })

            return articles

        except Exception as e:
            print(e)
            return []


if __name__ == "__main__":

    service = NewsService()

    news = service.get_news()

    for article in news:
        print(article["headline"])
        print(article["published"])
        print("------------------------")
