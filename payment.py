
class Payment:
    def __init__(self, policyholder, product, amount):
        self.policyholder = policyholder
        self.product = product
        self.amount = amount
        self.status = "Paid" if amount >= product.price else "Pending"

    def get_payment_info(self):
        return f"Payment for {self.policyholder.name}: {self.status}, Amount: {self.amount}"
