from typing import List

from movie_world.customer import Customer
from movie_world.dvd import DVD


class MovieWorld:
    _DVD_CAPACITY = 15
    _CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld._DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld._CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < self._CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self._DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [cust for cust in self.customers if cust.id == customer_id][0]

        for dvd in self.dvds:
            if dvd.id == dvd_id:
                if dvd.is_rented and dvd in customer.rented_dvds:
                    return f"{customer.name} has already rented {dvd.name}"
                elif dvd.is_rented:
                    return "DVD is already rented"
                elif customer.age < dvd.age_restriction:
                    return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                else:
                    dvd.is_rented = True
                    customer.rented_dvds.append(dvd)
                    return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = [cust for cust in self.customers if cust.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        return "\n".join(str(customer) for customer in self.customers) + "\n" \
               + "\n".join(str(dvd) for dvd in self.dvds)