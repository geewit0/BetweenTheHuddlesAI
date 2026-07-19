import sqlite3
import sys

sys.path.append("..")

from providers.espn_provider import ESPNProvider

DB_PATH = "../database/bth.db"


def search_local_team(query):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT
            name,
            city,
            abbreviation,
            conference,
            division
        FROM teams
        WHERE
            LOWER(name) LIKE LOWER(?)
            OR LOWER(city) LIKE LOWER(?)
            OR LOWER(abbreviation) LIKE LOWER(?)
    """, (
        f"%{query}%",
        f"%{query}%",
        f"%{query}%"
    ))

    team = cur.fetchone()

    conn.close()

    return team


def find_next_game(team_name):

    provider = ESPNProvider()

    data = provider.get_scoreboard()

    if not data:
        return None

    events = data.get("events", [])

    for event in events:

        game_name = event.get("name", "")

        if team_name.lower() in game_name.lower():

            status = (
                event.get("status", {})
                     .get("type", {})
                     .get("description", "Unknown")
            )

            return {
                "name": game_name,
                "date": event.get("date"),
                "status": status
            }

    return None


if __name__ == "__main__":

    query = input("Search team: ")

    team = search_local_team(query)

    if not team:
        print("Team not found.")
        sys.exit()

    print()
    print("===================================")
    print(" Between the Huddles AI")
    print("===================================")
    print()

    print("Team:", team[0])
    print("City:", team[1])
    print("Conference:", team[3])
    print("Division:", team[4])

    game = find_next_game(team[0])

    print()
    print("========== Next Game ==========")

    if game:
        print("Matchup:", game["name"])
        print("Date:", game["date"])
        print("Status:", game["status"])
    else:
        print("No upcoming game found.")
