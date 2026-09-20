# Here is a function that checks if a number is prime
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


# Here is a function that filters prime numbers
def filter_prime(numbers):
    prime_numbers = []

    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers


# Here is user input
user_input = input("Enter numbers separated by spaces: ")

# Here is a conversion from strings to integers
numbers = list(map(int, user_input.split()))

# Here is the result
print("Prime numbers:", filter_prime(numbers))