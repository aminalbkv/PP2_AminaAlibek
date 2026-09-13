# Example 1: Age check
age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")


# Example 2: Compare two numbers
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# Example 3: Even or odd number
number = 7

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# Example 4: Temperature
temperature = 22

if temperature > 30:
    print("It's hot outside")
elif temperature > 20:
    print("It's warm outside")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside")


# Example 5: Username
username = "Amina"

if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Username cannot be empty")