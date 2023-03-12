from typing import List
from Shop.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, prod_name: str) -> Product:
        for prod in self.products:
            if prod.name == prod_name:
                return prod

    def remove(self, prod_name: str) -> None:
        product = self.find(prod_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{p}: {p.quantity}" for p in self.products])