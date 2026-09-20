# Example 1: Function with return
# The function calculates the sum and returns the result

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum:", result)


# Example 2: Returning a list
# A function can return different data types

def get_fruits():
    return ["apple", "banana", "orange"]

fruits = get_fruits()
print("Fruits:", fruits)