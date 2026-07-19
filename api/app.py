from flask import Flask, jsonify
import sqlite3
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.game_service import GameService

app = Flask(__name__)

DB = os.path.join(
    os.path.dirname(__file__),
    "..",
    "database",
    "bth.db"
)

game_service = GameService()


@app.route("/")
def home():
    return jsonify({
        "app": "Between the Huddles AI",
        "status": "running",
        "version": "0.3"
    })


@app.route("/team/<team_name>")
def team(team_name):

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM teams
        WHERE LOWER(name) LIKE ?
           OR LOWER(city) LIKE ?
           OR LOWER(abbreviation) LIKE ?
    """, (
        f"%{team_name.lower()}%",
        f"%{team_name.lower()}%",
        f"%{team_name.lower()}%"
    ))

    row = cur.fetchone()

    conn.close()

    if row is None:
        return jsonify({"error": "Team not found"}), 404

    result = dict(row)

    abbreviation = result["abbreviation"]

    result["next_game"] = game_service.get_next_game(abbreviation)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
