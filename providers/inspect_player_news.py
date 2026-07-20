import requests
import json

PLAYER_ID = "3054850"  # Alvin Kamara

url = (
    f"https://site.api.espn.com/apis/site/v2/sports/"
    f"football/nfl/athletes/{PLAYER_ID}/news"
)

response = requests.get(url, timeout=15)

print("Status:", response.status_code)

try:
    data = response.json()
    print(json.dumps(data, indent=2)[:6000])
except Exception:
    print(response.text[:6000])
