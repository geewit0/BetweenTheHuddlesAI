import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from providers.espn_provider import ESPNProvider


class GameService:

    def __init__(self):
        self.provider = ESPNProvider()

    def get_next_game(self, abbreviation):

        scoreboard = self.provider.get_scoreboard()

        if not scoreboard:
            return None

        for event in scoreboard.get("events", []):

            competition = event.get("competitions", [{}])[0]

            competitors = competition.get("competitors", [])

            team_found = False
            opponent = None

            for competitor in competitors:

                team = competitor.get("team", {})

                if team.get("abbreviation") == abbreviation:
                    team_found = True
                else:
                    opponent = team.get("displayName")

            if team_found:
                return {
                    "matchup": event.get("name"),
                    "opponent": opponent,
                    "date": event.get("date"),
                    "status": competition["status"]["type"]["description"]
                }

        return None


if __name__ == "__main__":

    service = GameService()

    print(service.get_next_game("NO"))
