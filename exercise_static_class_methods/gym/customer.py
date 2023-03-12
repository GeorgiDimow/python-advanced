from gym.id import ID


class Customer(ID):
    def __init__(self, name: str, address: str, email: str):
        Customer.id += 1
        self.name = name
        self.address = address
        self.email = email

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address:" \
               f" {self.address}; Email: {self.email}"