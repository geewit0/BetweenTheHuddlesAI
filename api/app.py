from flask import Flask, jsonify
import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from services.team_service import TeamService


app = Flask(__name__)

team_service = TeamService()


@app.route("/")
def home():

    return jsonify({
        "app": "Between the Huddles AI",
        "status": "running",
        "version": "0.6"
    })


@app.route("/team/<team_name>")
def team(team_name):

    result = team_service.get_team(
        team_name
    )

    if result is None:
        return jsonify({
            "error": "Team not found"
        }), 404

    return jsonify(result)


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
