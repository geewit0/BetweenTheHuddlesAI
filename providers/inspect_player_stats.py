import json
import requests

url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/no/roster"

response = requests.get(url, timeout=15)

print("Status:", response.status_code)

data = response.json()

for group in data.get("athletes", []):
    for player in group.get("items", []):
        if player.get("id") == "3054850":
            print(json.dumps(player, indent=2))
            raise SystemExit

print("Player not found.")
