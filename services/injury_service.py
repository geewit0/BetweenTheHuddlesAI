import requests


class InjuryService:

    def __init__(self):
        self.url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/injuries"

    def get_injuries(self):
        response = requests.get(self.url, timeout=15)
        data = response.json()

        injuries = []

        for team in data.get("injuries", []):

            team_name = team.get("displayName")

            for injury in team.get("injuries", []):

                athlete = injury.get("athlete", {})

                injuries.append({
                    "player": athlete.get("displayName"),
                    "team": athlete.get("team", {}).get("abbreviation"),
                    "team_name": team_name,
                    "position": athlete.get("position", {}).get("abbreviation"),
                    "status": injury.get("status"),
                    "date": injury.get("date"),
                    "summary": injury.get("shortComment"),
                })

        return injuries


if __name__ == "__main__":
    service = InjuryService()

    injuries = service.get_injuries()

    print(f"Injuries found: {len(injuries)}")

    for injury in injuries[:20]:
        print(injury)
