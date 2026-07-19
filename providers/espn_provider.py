import requests


class ESPNProvider:

    BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl"

    def get_teams(self):
        try:
            response = requests.get(
                f"{self.BASE_URL}/teams",
                timeout=15
            )
            response.raise_for_status()
            return response.json()

        except Exception as e:
            print(f"Error loading teams: {e}")
            return None

    def get_scoreboard(self):
        try:
            response = requests.get(
                f"{self.BASE_URL}/scoreboard",
                timeout=15
            )
            response.raise_for_status()
            return response.json()

        except Exception as e:
            print(f"Error loading scoreboard: {e}")
            return None


if __name__ == "__main__":

    provider = ESPNProvider()

    data = provider.get_scoreboard()

    if not data:
        print("Unable to retrieve scoreboard.")
        exit()

    events = data.get("events", [])

    print(f"Games Found: {len(events)}")
    print()

    for game in events[:5]:
        print(game.get("name"))
        print(game.get("date"))
        print("----------------------------")
