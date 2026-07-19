from news_service import NewsService

news = NewsService()

articles = news.get_news(10)

for article in articles:
    print(article["headline"])
    print(article["description"])
    print("-" * 40)
