from gym.id import ID


class Equipment(ID):
    def __init__(self, name: str):
        Equipment.id += 1
        self.name = name

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"