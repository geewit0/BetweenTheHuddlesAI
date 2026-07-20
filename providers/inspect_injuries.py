import json
import requests

url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/no/injuries"

response = requests.get(url, timeout=15)

print("Status:", response.status_code)
print(json.dumps(response.json(), indent=2)[:8000])
