from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self._budget = budget
        self._animal_capacity = animal_capacity
        self._worker_capacity = worker_capacity

        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if price <= self._budget and len(self.animals) < self._animal_capacity:
            self.animals.append(animal)
            self._budget -= price
            return f"{self.name} the {animal.__class__.__name__} added to the zoo"
        elif price > self._budget and len(self.animals) < self._animal_capacity:
            return f"Not enough budget"
        else:
            return f"Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self._worker_capacity:
            self.workers.append(worker)
            return f"{self.name} the {worker.__class__.__name__} hired successfully"
        else:
            return f"Not enough space for worker"

    
