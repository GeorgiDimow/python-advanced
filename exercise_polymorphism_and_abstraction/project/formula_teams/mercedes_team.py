from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        latest_budget = self.budget
        self.budget -= 200000
        if race_pos <= 1:
            self.budget += 1000000
        elif race_pos <= 2:
            self.budget += 500000
        if race_pos <= 8:
            self.budget += 100000
        elif race_pos <= 10:
            self.budget += 50000

        return f"The revenue after thе race is {self.budget - latest_budget}$. Current budget {self.budget}$"
