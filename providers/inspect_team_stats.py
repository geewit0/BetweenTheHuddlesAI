import json
import requests

url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/no/statistics"

response = requests.get(url, timeout=15)

print("Status:", response.status_code)

try:
    data = response.json()
    print(json.dumps(data, indent=2)[:12000])
except Exception:
    print(response.text[:12000])
