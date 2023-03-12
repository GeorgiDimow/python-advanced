from gym.id import ID


class Trainer(ID):
    def __init__(self, name: str):
        Trainer.id += 1
        self.name = name

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"