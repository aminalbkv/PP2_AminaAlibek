# Example 4: Methods with parameters

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calculator = Calculator()

print("Addition:", calculator.add(5, 3))
print("Multiplication:", calculator.multiply(4, 7))