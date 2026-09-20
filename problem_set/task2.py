# Here is a function that converts Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


# Here is user input
fahrenheit = float(input("Enter Fahrenheit: "))

# Here is the result
print("Celsius:", fahrenheit_to_celsius(fahrenheit))