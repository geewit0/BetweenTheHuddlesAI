import requests


class StandingsService:

    def __init__(self):
        self.url = (
            "http://sports.core.api.espn.com/v2/"
            "sports/football/leagues/nfl/"
            "seasons/2025/types/2/groups/9/"
            "standings/2?lang=en&region=us"
        )

    def get_standings(self):

        response = requests.get(self.url, timeout=15)
        data = response.json()

        standings = []

        for team in data.get("standings", []):

            team_ref = team.get("team", {}).get("$ref", "")

            team_response = requests.get(team_ref, timeout=15)
            team_data = team_response.json()

            record = team.get("records", [{}])[0]

            standings.append({
                "team": team_data.get("displayName"),
                "abbreviation": team_data.get("abbreviation"),
                "record": record.get("summary"),
            })

        return standings


if __name__ == "__main__":

    service = StandingsService()

    standings = service.get_standings()

    print(f"Teams found: {len(standings)}")

    for team in standings:
        print(team)
