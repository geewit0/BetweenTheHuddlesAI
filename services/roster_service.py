import requests


class RosterService:

    def __init__(self):
        self.base_url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"

        self.team_map = {
            "saints": "no",
            "new orleans": "no",
            "no": "no"
        }

    def get_roster(self, team="no"):

        team = self.team_map.get(
            team.lower(),
            team.lower()
        )

        try:

            response = requests.get(
                f"{self.base_url}/{team}/roster",
                timeout=10
            )

            data = response.json()

            roster = []

            for group in data.get("athletes", []):

                group_name = group.get("position")

                for player in group.get("items", []):

                    roster.append({
                        "id": player.get("id"),
                        "name": player.get("displayName"),
                        "position_group": group_name,
                        "position": player.get("position", {}).get("abbreviation"),
                        "age": player.get("age"),
                        "height": player.get("displayHeight"),
                        "weight": player.get("displayWeight")
                    })

            return roster

        except Exception as e:

            print("Roster Error:", e)
            return []


if __name__ == "__main__":

    service = RosterService()

    roster = service.get_roster("saints")

    print(f"Players found: {len(roster)}")

    for player in roster[:10]:
        print(player)
