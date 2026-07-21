class AIService:

    def analyze_team(self, team):
        analysis = []

        analysis.append(
            f"{team['name']} currently competes in the "
            f"{team['conference']} {team['division']}."
        )

        if team.get("next_game"):
            analysis.append(
                f"The next matchup is against "
                f"{team['next_game']['opponent']}."
            )

        if len(team.get("injuries", [])) > 0:
            analysis.append(
                f"The team currently has "
                f"{len(team['injuries'])} players listed on the injury report."
            )

        if len(team.get("news", [])) > 0:
            analysis.append(
                "Recent news suggests there are several important storylines "
                "surrounding this team."
            )

        analysis.append(
            "A full AI prediction engine will be added in a future update."
        )

        return " ".join(analysis)
