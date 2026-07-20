import requests

class InjuryService:
    def __init__(self):
        self.url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/injuries"

    def get_injuries(self, team=None, limit=5):
        response = requests.get(self.url, timeout=15)
        data = response.json()

        injuries = []

        for injury_team in data.get("injuries", []):
            for injury in injury_team.get("injuries", []):
                athlete = injury.get("athlete", {})

                if team:
                    if athlete.get("team", {}).get("abbreviation", "").lower() != team.lower():
                        continue

                injuries.append({
                    "player": athlete.get("displayName"),
                    "position": athlete.get("position", {}).get("abbreviation"),
                    "status": injury.get("status"),
                    "date": injury.get("date"),
                    "summary": injury.get("shortComment")
                })

                if len(injuries) >= limit:
                    return injuries

        return injuries


if __name__ == "__main__":
    service = InjuryService()
    print(service.get_injuries("NO"))
