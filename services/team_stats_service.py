import requests

from services.team_mapper import get_team_id


class TeamStatsService:

    def __init__(self):
        self.base_url = (
            "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"
        )

    def get_stats(self, team="no"):

        team = get_team_id(team)

        try:

            response = requests.get(
                f"{self.base_url}/{team}/statistics",
                timeout=15
            )

            data = response.json()

            categories = (
                data.get("results", {})
                .get("stats", {})
                .get("categories", [])
            )

            stats = []

            for category in categories:

                category_name = category.get("displayName")

                for stat in category.get("stats", []):

                    stats.append({
                        "category": category_name,
                        "name": stat.get("displayName"),
                        "value": stat.get("displayValue")
                    })

            return stats

        except Exception as e:

            print("Team Stats Error:", e)
            return []


if __name__ == "__main__":

    service = TeamStatsService()

    stats = service.get_stats()

    print(f"Stats found: {len(stats)}")

    for stat in stats[:20]:
        print(stat)
