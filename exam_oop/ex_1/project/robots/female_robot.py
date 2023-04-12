from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):

    @property
    def get_weight(self):
        return 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.get_weight)

    def eating(self):
        self.weight += 1
