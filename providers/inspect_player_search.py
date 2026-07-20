import requests
import json


url = "https://site.web.api.espn.com/apis/common/v3/search"


response = requests.get(
    url,
    params={
        "region": "us",
        "lang": "en",
        "query": "Alvin Kamara"
    },
    timeout=10
)


print("Status:", response.status_code)

print(
    json.dumps(
        response.json(),
        indent=2
    )[:5000]
)
