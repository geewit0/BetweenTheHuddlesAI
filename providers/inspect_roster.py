import requests
import json


url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/no/roster"


response = requests.get(
    url,
    timeout=10
)


print("Status:", response.status_code)

print(
    json.dumps(
        response.json(),
        indent=2
    )[:5000]
)
