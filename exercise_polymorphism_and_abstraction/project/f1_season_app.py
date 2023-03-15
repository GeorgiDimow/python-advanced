from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    valid_names = ["Red Bull", "Mercedes"]
    def __init__(self):
        self.red_bull_team: RedBullTeam = None
        self.mercedes_team: MercedesTeam = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in self.valid_names:
            if team_name == "":
                pass
        else:
            raise ValueError