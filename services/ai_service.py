class AIService:
    def analyze_team(self, team):
        injuries = team.get("injuries", [])
        news = team.get("news", [])
        next_game = team.get("next_game", {})

        questionable = [
            i for i in injuries
            if i.get("status", "").lower() == "questionable"
        ]

        active = [
            i for i in injuries
            if i.get("status", "").lower() == "active"
        ]

        summary = (
            f"{team['name']} will open the season against "
            f"{next_game.get('opponent', 'their opponent')}."
        )

        if questionable:
            summary += (
                f" The team currently has {len(questionable)} "
                "questionable player(s) to monitor."
            )
        else:
            summary += " The roster appears relatively healthy."

        offense = (
            "The offense should focus on protecting the quarterback "
            "and establishing a consistent running game."
        )

        if any(i["position"] == "RB" for i in active):
            offense += (
                " The running back room provides solid depth entering "
                "the matchup."
            )

        defense = (
            "The defense's priority will be generating pressure, "
            "forcing turnovers, and limiting explosive plays."
        )

        prediction = (
            f"{team['name']} has a realistic opportunity to win if "
            "they protect the football and control the line of scrimmage."
        )

        if news:
            prediction += (
                f" Recent headline: {news[0]['headline']}"
            )

        return {
            "summary": summary,
            "offense": offense,
            "defense": defense,
            "prediction": prediction
        }
