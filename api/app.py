from flask import Flask, jsonify, render_template_string

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

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

body{
background:#111;
color:white;
font-family:Arial,sans-serif;
margin:0;
padding:0;
text-align:center;
}

header{
background:#00b7ff;
padding:25px;
}

h1{
margin:0;
font-size:38px;
}

p{
color:#ddd;
}

.container{
padding:30px;
}

input{
width:90%;
max-width:500px;
padding:15px;
font-size:18px;
border-radius:10px;
border:none;
margin-bottom:30px;
}

.grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
gap:15px;
max-width:900px;
margin:auto;
}

.team{
background:#222;
padding:18px;
border-radius:12px;
text-decoration:none;
color:white;
font-weight:bold;
transition:.2s;
}

.team:hover{
background:#00b7ff;
}

footer{
margin-top:40px;
color:#888;
font-size:14px;
}

</style>

</head>

<body>

<header>

<h1>🏈 BetweenTheHuddlesAI</h1>

<p>Your AI NFL Headquarters</p>

</header>

<div class="container">

<input
placeholder="Search coming soon..."
disabled
>

<div class="grid">

<a class="team" href="/team/ARI">Arizona Cardinals</a>
<a class="team" href="/team/ATL">Atlanta Falcons</a>
<a class="team" href="/team/B
