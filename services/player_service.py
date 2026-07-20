import requests


class PlayerService:

    def __init__(self):
        self.base_url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"

    def get_player(self, team="no", player_id=None):

        if player_id is None:
            return None

        try:

            response = requests.get(
                f"{self.base_url}/{team}/roster",
                timeout=15
            )

            data = response.json()

            for group in data.get("athletes", []):

                for player in group.get("items", []):

                    if str(player.get("id")) == str(player_id):

                        return {
                            "id": player.get("id"),
                            "name": player.get("displayName"),
                            "position": player.get("position", {}).get("abbreviation"),
                            "age": player.get("age"),
                            "height": player.get("displayHeight"),
                            "weight": player.get("displayWeight"),
                            "birthDate": player.get("dateOfBirth"),
                            "experience": player.get("experience", {}).get("years"),
                            "college": (
                                player.get("college", {})
                                .get("name")
                                if player.get("college")
                                else None
                            )
                        }

            return None

        except Exception as e:
            print("Player Error:", e)
            return None


if __name__ == "__main__":

    service = PlayerService()

    print(service.get_player("no", "3054850"))
