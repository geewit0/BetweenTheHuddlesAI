import requests

from services.team_mapper import get_team_id


class ScheduleService:

    def __init__(self):
        self.base_url = (
            "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"
        )

    def get_schedule(self, team="no"):

        team = get_team_id(team)

        try:

            response = requests.get(
                f"{self.base_url}/{team}/schedule",
                timeout=15
            )

            data = response.json()

            games = []

            for event in data.get("events", []):

                competition = event.get("competitions", [{}])[0]

                competitors = competition.get("competitors", [])

                home = next(
                    (
                        c for c in competitors
                        if c.get("homeAway") == "home"
                    ),
                    {}
                )

                away = next(
                    (
                        c for c in competitors
                        if c.get("homeAway") == "away"
                    ),
                    {}
                )

                games.append({
                    "id": event.get("id"),
                    "date": event.get("date"),
                    "status": competition.get("status", {}).get("type", {}).get("description"),
                    "home_team": home.get("team", {}).get("displayName"),
                    "away_team": away.get("team", {}).get("displayName"),
                    "home_score": home.get("score"),
                    "away_score": away.get("score")
                })

            return games

        except Exception as e:

            print("Schedule Error:", e)
            return []


if __name__ == "__main__":

    service = ScheduleService()

    schedule = service.get_schedule("saints")

    print(f"Games found: {len(schedule)}")

    for game in schedule[:5]:
        print(game)
