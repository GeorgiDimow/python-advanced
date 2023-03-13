from typing import List

from wild_cat_zoo.animal import Animal
from wild_cat_zoo.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self._Zoo__budget = budget
        self._Zoo__animal_capacity = animal_capacity
        self._Zoo__workers_capacity = worker_capacity

        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if price <= self._Zoo__budget and len(self.animals) < self._Zoo__animal_capacity:
            self.animals.append(animal)
            self._Zoo__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif price > self._Zoo__budget and len(self.animals) < self._Zoo__animal_capacity:
            return f"Not enough budget"
        else:
            return f"Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self._Zoo__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return f"Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salary = sum([worker.salary for worker in self.workers])
        if sum_salary <= self._Zoo__budget:
            self._Zoo__budget -= sum_salary
            return f"You payed your workers. They are happy. Budget left: {self._Zoo__budget}"
        else:
            return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_cost = sum([animal.money_for_care for animal in self.animals])
        if sum_cost <= self._Zoo__budget:
            self._Zoo__budget -= sum_cost
            return f"You tended all the animals. They are happy. Budget left: {self._Zoo__budget}"
        else:
            return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self._Zoo__budget += amount

    def animals_status(self):
        lions = '\n'.join([f"{animal}" for animal in self.animals if animal.__class__.__name__ == 'Lion'])
        tigers = '\n'.join([f"{animal}" for animal in self.animals if animal.__class__.__name__ == 'Tiger'])
        cheetahs = '\n'.join([f"{animal}" for animal in self.animals if animal.__class__.__name__ == 'Cheetah'])
        return f"You have {len(self.animals)} animals\n" \
               f"----- {len([animal for animal in self.animals if animal.__class__.__name__ == 'Lion'])} Lions:\n" \
               f"{lions}\n" \
               f"----- {len([animal for animal in self.animals if animal.__class__.__name__ == 'Tiger'])} Tigers:\n" \
               f"{tigers}\n" \
               f"----- {len([animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah'])} Cheetahs:\n" \
               f"{cheetahs}"

    def workers_status(self):
        vet = '\n'.join([f"{worker}" for worker in self.workers if worker.__class__.__name__ == 'Vet'])
        caretaker = '\n'.join([f"{worker}" for worker in self.workers if worker.__class__.__name__ == 'Caretaker'])
        keeper = '\n'.join([f"{worker}" for worker in self.workers if worker.__class__.__name__ == 'Keeper'])
        return f"You have {len(self.workers)} workers\n" \
               f"----- {len([worker for worker in self.workers if worker.__class__.__name__ == 'Keeper'])} Keepers:\n" \
               f"{keeper}\n" \
               f"----- {len([worker for worker in self.workers if worker.__class__.__name__ == 'Caretaker'])} Caretakers:\n" \
               f"{caretaker}\n" \
               f"----- {len([worker for worker in self.workers if worker.__class__.__name__ == 'Vet'])} Vets:\n" \
               f"{vet}"




