import requests


class NewsService:

    def __init__(self):

        self.team_ids = {
            "saints": "no",
            "new orleans saints": "no",
            "cowboys": "dal",
            "eagles": "phi",
            "packers": "gb",
            "49ers": "sf",
            "lions": "det",
            "chiefs": "kc",
            "bills": "buf"
        }


    def get_news(self, limit=5, team=None):

        try:

            if team and team.lower() in self.team_ids:

                abbreviation = self.team_ids[team.lower()]

                url = (
                    "https://site.api.espn.com/apis/site/v2/"
                    f"sports/football/nfl/news?team={abbreviation}"
                )

            else:

                url = (
                    "https://site.api.espn.com/apis/site/v2/"
                    "sports/football/nfl/news"
                )


            response = requests.get(
                url,
                timeout=10
            )

            data = response.json()

            articles = data.get("articles", [])

            results = []

            for article in articles:

                results.append({
                    "headline": article.get("headline"),
                    "description": article.get("description"),
                    "published": article.get("published"),
                    "link": article.get("links", {})
                        .get("web", {})
                        .get("href")
                })

                if len(results) >= limit:
                    break


            return results


        except Exception as e:

            print("News Error:", e)
            return []


if __name__ == "__main__":

    news = NewsService()

    articles = news.get_news(
        5,
        "saints"
    )

    for article in articles:

        print(article["headline"])
        print(article["description"])
        print("-" * 40)
