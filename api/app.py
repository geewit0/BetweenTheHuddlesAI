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

HOME = """
<!DOCTYPE html>
<html>
<head>
<title>BetweenTheHuddlesAI</title>
<style>
body{
background:#111;
color:white;
font-family:Arial,sans-serif;
text-align:center;
padding:40px;
}
.container{
max-width:900px;
margin:auto;
background:#222;
padding:30px;
border-radius:15px;
}
select,button{
padding:12px;
font-size:18px;
margin:10px;
border-radius:8px;
border:none;
}
button{
background:#00b7ff;
color:white;
cursor:pointer;
}
button:hover{
background:#0095d6;
}
</style>
</head>
<body>

<div class="container">

<h1>🏈 BetweenTheHuddlesAI</h1>

<h2>Select Your NFL Team</h2>

<select id="team">
<option value="cardinals">Arizona Cardinals</option>
<option value="falcons">Atlanta Falcons</option>
<option value="ravens">Baltimore Ravens</option>
<option value="bills">Buffalo Bills</option>
<option value="panthers">Carolina Panthers</option>
<option value="bears">Chicago Bears</option>
<option value="bengals">Cincinnati Bengals</option>
<option value="browns">Cleveland Browns</option>
<option value="cowboys">Dallas Cowboys</option>
<option value="broncos">Denver Broncos</option>
<option value="lions">Detroit Lions</option>
<option value="packers">Green Bay Packers</option>
<option value="texans">Houston Texans</option>
<option value="colts">Indianapolis Colts</option>
<option value="jaguars">Jacksonville Jaguars</option>
<option value="chiefs">Kansas City Chiefs</option>
<option value="raiders">Las Vegas Raiders</option>
<option value="chargers">Los Angeles Chargers</option>
<option value="rams">Los Angeles Rams</option>
<option value="dolphins">Miami Dolphins</option>
<option value="vikings">Minnesota Vikings</option>
<option value="patriots">New England Patriots</option>
<option value="saints" selected>New Orleans Saints</option>
<option value="giants">New York Giants</option>
<option value="jets">New York Jets</option>
<option value="eagles">Philadelphia Eagles</option>
<option value="steelers">Pittsburgh Steelers</option>
<option value="49ers">San Francisco 49ers</option>
<option value="seahawks">Seattle Seahawks</option>
<option value="buccaneers">Tampa Bay Buccaneers</option>
<option value="titans">Tennessee Titans</option>
<option value="commanders">Washington Commanders</option>
</select>

<br>

<button onclick="go()">View Team</button>

</div>

<script>
function go(){
let team=document.getElementById("team").value;
window.location="/team/"+team;
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return HOME

@app.route("/health")
def health():
    return jsonify({"status":"online"})

@app.route("/team/<team>")
def team(team):
    result = teams.get_team(team)
    if result is None:
        return jsonify({"error":"Team not found"}),404
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
