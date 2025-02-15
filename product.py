
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def update_price(self, new_price):
        self.price = new_price

    def get_product_info(self):
        return f"Product: {self.name}, ID: {self.product_id}, Price: {self.price}"
