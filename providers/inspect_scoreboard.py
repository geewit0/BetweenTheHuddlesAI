import json
from espn_provider import ESPNProvider

provider = ESPNProvider()

data = provider.get_scoreboard()

if not data:
    print("Unable to retrieve data.")
    exit()

events = data.get("events", [])

if not events:
    print("No games found.")
    exit()

first_game = events[0]

print(json.dumps(first_game, indent=2))
