import sqlite3
import os

from services.game_service import GameService
from services.news_service import NewsService
from services.injury_service import InjuryService


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
        self.injuries = InjuryService()


    def get_all_teams(self):
        conn = sqlite3.connect(self.db)
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()

        cur.execute("""
        SELECT *
        FROM teams
        ORDER BY name
        """)

        rows = cur.fetchall()
        conn.close()

        teams = [dict(row) for row in rows]

        for team in teams:
            team["slug"] = team["name"].lower().replace(" ", "-")

        return teams


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
           OR LOWER(REPLACE(name, ' ', '-')) LIKE ?
        """, (
            f"%{search.lower()}%",
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
            search
        )

        team["injuries"] = self.injuries.get_injuries(
            team["abbreviation"]
        )

        return team


    def get_team_stats(self, team_name):
        conn = sqlite3.connect(self.db)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("""
            SELECT
                ts.wins,
                ts.losses,
                ts.ties,
                ts.division_rank,
                ts.points_per_game,
                ts.points_allowed_per_game,
                ts.passing_yards_per_game,
                ts.rushing_yards_per_game,
                ts.offense_rank,
                ts.defense_rank,
                ts.turnover_differential
            FROM team_stats ts
            JOIN teams t
                ON ts.team_id = t.id
            WHERE LOWER(t.name) LIKE ?
               OR LOWER(REPLACE(t.name, ' ', '-')) = ?
               OR LOWER(t.abbreviation) = ?
        """, (
            f"%{team_name.lower()}%",
            team_name.lower(),
            team_name.lower()
        ))

        row = cur.fetchone()
        conn.close()

        if row is None:
            return {
                "record": "0-0",
                "division_rank": "TBD",
                "ppg": "0.0",
                "oppg": "0.0",
                "pass_yards": "0.0",
                "rush_yards": "0.0",
                "offense_rank": "TBD",
                "defense_rank": "TBD",
                "turnover_diff": "0"
            }

        return {
            "record": f"{row['wins']}-{row['losses']}" + (f"-{row['ties']}" if row["ties"] else ""),
            "division_rank": row["division_rank"],
            "ppg": row["points_per_game"],
            "oppg": row["points_allowed_per_game"],
            "pass_yards": row["passing_yards_per_game"],
            "rush_yards": row["rushing_yards_per_game"],
            "offense_rank": row["offense_rank"],
            "defense_rank": row["defense_rank"],
            "turnover_diff": row["turnover_differential"]
        }

if __name__ == "__main__":
    service = TeamService()
    print(service.get_team("saints"))
