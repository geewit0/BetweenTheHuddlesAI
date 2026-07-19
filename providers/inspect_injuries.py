import requests
import re


url = "https://www.espn.com/nfl/team/injuries/_/name/no"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=10
)

html = response.text

patterns = [
    r'https://[^"]+api[^"]+',
    r'//[^"]+api[^"]+',
    r'athlete[^"]+',
    r'injury[^"]+'
]

for pattern in patterns:
    print("\nPATTERN:", pattern)

    matches = re.findall(
        pattern,
        html,
        re.IGNORECASE
    )

    for match in matches[:10]:
        print(match)
