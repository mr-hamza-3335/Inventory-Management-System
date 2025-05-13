from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, quantity_in_stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    @abstractmethod
    def restock(self, amount):
        pass

    @abstractmethod
    def sell(self, quantity):
        pass

    @abstractmethod
    def get_total_value(self):
        pass

    def __str__(self):
        return (f"ID: {self._product_id}, Name: {self._name}, "
                f"Price: ${self._price}, Stock: {self._quantity_in_stock}")
