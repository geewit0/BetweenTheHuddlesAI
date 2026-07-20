import requests
import json

url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2025/types/2/groups/9/standings/2?lang=en&region=us"

response = requests.get(url, timeout=15)

print("Status:", response.status_code)
print(json.dumps(response.json(), indent=2))
