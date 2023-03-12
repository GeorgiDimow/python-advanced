from typing import List

from gym.customer import Customer
from gym.equipment import Equipment
from gym.exercise_plan import ExercisePlan
from gym.subscription import Subscription
from gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.subscriptions: List[Subscription] = []
        self.plans: List[ExercisePlan] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        customer_id, trainer_id, plan_id = self.subscriptions[subscription_id-1].customer_id, self.subscriptions[subscription_id-1].trainer_id, self.subscriptions[subscription_id-1].exercise_id
        equipment_id = self.plans[plan_id-1].equipment_id

        return f"{self.subscriptions[subscription_id-1]}\n" \
               f"{self.customers[customer_id-1]}\n" \
               f"{self.trainers[trainer_id-1]}\n" \
               f"{self.equipment[equipment_id-1]}\n" \
               f"{self.plans[plan_id-1]}\n"