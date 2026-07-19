import requests


class NFLDataEngine:

    def __init__(self):
        print("Initializing NFL Data Engine...")

    def status(self):
        return "READY"

    def test_connection(self):
        try:
            response = requests.get(
                "https://www.google.com",
                timeout=15
            )

            if response.status_code == 200:
                return "Internet connection successful."

            return f"Connection failed: {response.status_code}"

        except Exception as e:
            return f"Error: {e}"


if __name__ == "__main__":
    engine = NFLDataEngine()

    print(engine.status())
    print(engine.test_connection())
