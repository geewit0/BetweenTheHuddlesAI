import requests


class LiveScoresService:

    def __init__(self):
        self.url = (
            "https://site.api.espn.com/apis/site/v2/sports/"
            "football/nfl/scoreboard"
        )

    def get_scores(self):

        response = requests.get(self.url, timeout=15)
        data = response.json()

        games = []

        for event in data.get("events", []):

            competition = event["competitions"][0]

            home = None
            away = None

            for team in competition["competitors"]:

                info = {
                    "team": team["team"]["displayName"],
                    "abbreviation": team["team"]["abbreviation"],
                    "score": team["score"],
                    "winner": team.get("winner", False),
                }

                if team["homeAway"] == "home":
                    home = info
                else:
                    away = info

            games.append({
                "id": event["id"],
                "name": event["name"],
                "status": competition["status"]["type"]["description"],
                "home": home,
                "away": away,
            })

        return games


if __name__ == "__main__":

    service = LiveScoresService()

    games = service.get_scores()

    print(f"Games found: {len(games)}")

    for game in games:
        print(game)
