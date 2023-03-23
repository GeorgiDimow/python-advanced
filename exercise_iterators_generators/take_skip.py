class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.iterations = -1
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count - 1:
            raise StopIteration

        self.iterations += 1

        return self.iterations * self.step

