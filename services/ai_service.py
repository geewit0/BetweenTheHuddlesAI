import random


class AIService:

    def analyze_team(self, team):
        team_name = team["name"]

        opponent = "their opponent"
        if team.get("next_game"):
            opponent = team["next_game"].get("opponent", opponent)

        injuries = team.get("injuries", [])
        injury_count = len(injuries)

        offense_options = [
            "The offense should establish the running game early while protecting the quarterback. Sustained drives will be important.",
            "Success will depend on winning first down and limiting negative plays. A balanced offensive attack gives the best chance to control the game.",
            "Explosive plays will be important, but avoiding turnovers will matter even more."
        ]

        defense_options = [
            "Generating pressure without giving up explosive plays should be the defense's primary focus.",
            "The defense must force third-and-long situations and create turnovers whenever possible.",
            "Stopping the run early will allow the defense to attack opposing quarterbacks more aggressively."
        ]

        if injury_count == 0:
            summary = (
                f"{team_name} enters its next matchup against {opponent} with a healthy roster. "
                "Depth across the team should provide flexibility on both sides of the ball."
            )
        elif injury_count <= 3:
            summary = (
                f"{team_name} has a few injury concerns heading into the matchup with {opponent}, "
                "but most key contributors are expected to be available."
            )
        else:
            summary = (
                f"{team_name} is dealing with several injuries entering the game against {opponent}. "
                "Depth players may have larger roles than expected."
            )

        if injury_count >= 4:
            prediction = (
                f"If {team_name} can overcome its injury concerns and avoid turnovers, it has a realistic chance to defeat {opponent}."
            )
        else:
            prediction = (
                f"{team_name} has a solid opportunity to defeat {opponent} if it controls the line of scrimmage and wins the turnover battle."
            )

        return {
            "summary": summary,
            "offense": random.choice(offense_options),
            "defense": random.choice(defense_options),
            "prediction": prediction
        }
