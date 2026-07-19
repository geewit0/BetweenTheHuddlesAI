import requests
from bs4 import BeautifulSoup


class InjuryService:

    def __init__(self):
        self.url = "https://www.espn.com/nfl/team/injuries/_/name/no"


    def get_injuries(self, limit=10):

        try:
            response = requests.get(
                self.url,
                headers={
                    "User-Agent": "Mozilla/5.0"
                },
                timeout=10
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            injuries = []

            players = soup.select(
                ".Athlete__PlayerName"
            )

            for player in players:

                container = player

                for _ in range(5):
                    container = container.parent

                text = container.get_text(
                    " | ",
                    strip=True
                )

                parts = text.split(" | ")

                if len(parts) >= 5:

                    injuries.append({
                        "player": parts[0],
                        "position": parts[1],
                        "status": parts[3],
                        "details": parts[4]
                    })

                if len(injuries) >= limit:
                    break

            return injuries


        except Exception as e:
            print("Injury Error:", e)
            return []


if __name__ == "__main__":

    service = InjuryService()

    for injury in service.get_injuries():
        print(injury)
