from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        latest_budget = self.budget
        self.budget -= 250000
        if race_pos <= 1:
            self.budget += 1500000
        elif race_pos <= 2:
            self.budget += 800000
        if race_pos <= 8:
            self.budget += 20000
        elif race_pos <= 10:
            self.budget += 10000

        return f"The revenue after thе race is {self.budget - latest_budget}$. Current budget {self.budget}$"
