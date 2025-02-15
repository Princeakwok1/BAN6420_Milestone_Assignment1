from policyholder import Policyholder
from product import Product
from payment import Payment

# Create Products
product1 = Product(101, "Health Insurance", 500)
product2 = Product(102, "Housing Insurance", 800)

# Create Policyholders
policyholder1 = Policyholder("Kunle Afolarin", "P001")
policyholder2 = Policyholder("Daniel Cooker", "P002")

# Process Payments
payment1 = Payment(policyholder1, product1, 500)
payment2 = Payment(policyholder2, product2, 800)

# Display Information
print(policyholder1.get_details())
print(policyholder2.get_details())
print(product1.get_product_info())
print(product2.get_product_info())
print(payment1.get_payment_info())
print(payment2.get_payment_info())

