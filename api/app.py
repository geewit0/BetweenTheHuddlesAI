from flask import Flask, jsonify

from services.team_service import TeamService
from services.roster_service import RosterService
from services.player_service import PlayerService
from services.schedule_service import ScheduleService
from services.team_stats_service import TeamStatsService
from services.standings_service import StandingsService
from services.live_scores_service import LiveScoresService
from services.injury_service import InjuryService

app = Flask(__name__)

teams = TeamService()
roster = RosterService()
players = PlayerService()
schedule = ScheduleService()
team_stats = TeamStatsService()
standings = StandingsService()
scores = LiveScoresService()
injuries = InjuryService()


@app.route("/")
def home():
    return jsonify({
        "name": "BetweenTheHuddlesAI API",
        "status": "online",
        "version": "1.0"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/team/<team>")
def team(team):
    result = teams.get_team(team)
    if result is None:
        return jsonify({"error": "Team not found"}), 404
    return jsonify(result)


@app.route("/team/<team>/roster")
def team_roster(team):
    return jsonify(roster.get_roster(team))


@app.route("/team/<team>/player/<player_id>")
def team_player(team, player_id):
    return jsonify(players.get_player(player_id))


@app.route("/team/<team>/schedule")
def team_schedule(team):
    return jsonify(schedule.get_schedule(team))


@app.route("/team/<team>/stats")
def team_stats_route(team):
    return jsonify(team_stats.get_stats(team))


@app.route("/standings")
def standings_route():
    return jsonify(standings.get_standings())


@app.route("/scores")
def scores_route():
    return jsonify(scores.get_scores())


@app.route("/injuries")
def injuries_route():
    return jsonify(injuries.get_injuries())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
