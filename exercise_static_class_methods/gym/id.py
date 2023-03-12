class ID:
    id = 0

    def __init__(self):
        self.id += 1

    @classmethod
    def get_next_id(cls):
        return cls.id + 1