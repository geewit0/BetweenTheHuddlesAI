import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sqlite3
from services.team_stats_service import TeamStatsService
DB = "database/bth.db"


def value(stats, name, default=0):
    for stat in stats:
        if stat["name"] == name:
            try:
                return float(str(stat["value"]).replace(",", ""))
            except Exception:
                try:
                    return float(str(stat["value"]).replace("%", ""))
                except Exception:
                    return default
    return default


def update_team(team_name, team_id):
    service = TeamStatsService()
    stats = service.get_stats(team_name)

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        UPDATE team_stats
        SET
            points_per_game=?,
            passing_yards_per_game=?,
            rushing_yards_per_game=?
        WHERE team_id=?
    """, (
    value(stats, "Total Points Per Game"),
    value(stats, "Passing Yards Per Game"),
    value(stats, "Rushing Yards Per Game"),
    team_id
))

    conn.commit()
    conn.close()

    print(f"Updated {team_name}")


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        SELECT id, name
        FROM teams
        ORDER BY id
    """)

    teams = cur.fetchall()
    conn.close()

    for team_id, team_name in teams:
        nickname = team_name.split()[-1].lower()

        if nickname == "49ers":
            nickname = "49ers"

        update_team(nickname, team_id)

    print("\nFinished updating all team stats.")


if __name__ == "__main__":
    main()
