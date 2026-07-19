import sqlite3
import os

from services.game_service import GameService
from services.news_service import NewsService


class TeamService:

    def __init__(self):

        self.db = os.path.join(
            os.path.dirname(__file__),
            "..",
            "database",
            "bth.db"
        )

        self.games = GameService()
        self.news = NewsService()


    def get_team(self, search):

        conn = sqlite3.connect(self.db)
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()

        cur.execute("""
        SELECT *
        FROM teams
        WHERE LOWER(name) LIKE ?
           OR LOWER(city) LIKE ?
           OR LOWER(abbreviation) LIKE ?
        """, (
            f"%{search.lower()}%",
            f"%{search.lower()}%",
            f"%{search.lower()}%"
        ))

        row = cur.fetchone()

        conn.close()


        if row is None:
            return None


        team = dict(row)


        team["next_game"] = self.games.get_next_game(
            team["abbreviation"]
        )


        team["news"] = self.news.get_news(
            3,
            team["name"]
        )


        return team



if __name__ == "__main__":

    service = TeamService()

    print(service.get_team("saints"))
