import json
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from custom_exceptions import *

class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product._product_id in self._products:
            raise DuplicateProductIDError("Product ID already exists.")
        self._products[product._product_id] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            del self._products[product_id]

    def sell_product(self, product_id, quantity):
        if product_id not in self._products:
            raise ValueError("Product ID not found.")
        product = self._products[product_id]
        product.sell(quantity)

    def restock_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].restock(quantity)

    def list_all_products(self):
        return [str(p) for p in self._products.values()]

    def search_by_name(self, name):
        return [str(p) for p in self._products.values() if name.lower() in p._name.lower()]

    def search_by_type(self, product_type):
        return [str(p) for p in self._products.values() if p.__class__.__name__.lower() == product_type.lower()]

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        to_remove = []
        for pid, product in self._products.items():
            if isinstance(product, Grocery) and product.is_expired():
                to_remove.append(pid)
        for pid in to_remove:
            del self._products[pid]

    def save_to_file(self, filename):
        data = []
        for p in self._products.values():
            product_data = p.__dict__.copy()
            product_data["type"] = p.__class__.__name__
            if isinstance(p, Grocery):
                product_data["expiry_date"] = p.expiry_date.strftime("%Y-%m-%d")
            data.append(product_data)

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            for item in data:
                type_ = item.pop("type")
                if type_ == "Electronics":
                    product = Electronics(**item)
                elif type_ == "Grocery":
                    product = Grocery(**item)
                elif type_ == "Clothing":
                    product = Clothing(**item)
                else:
                    raise InvalidProductDataError("Unknown product type.")
                self.add_product(product)
        except Exception as e:
            raise InvalidProductDataError(str(e))
