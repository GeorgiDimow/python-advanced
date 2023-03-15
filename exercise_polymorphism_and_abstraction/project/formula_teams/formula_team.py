from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        if budget < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        else:
            self.budget = budget

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        ...