# Example 5: __str__ magic method

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs {self.price} tenge"


product1 = Product("Laptop", 350000)
product2 = Product("Phone", 250000)

print(product1)
print(product2)