import json
import requests

url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/standings"

response = requests.get(url, timeout=15)
response.raise_for_status()

data = response.json()

print(json.dumps(data, indent=2))
