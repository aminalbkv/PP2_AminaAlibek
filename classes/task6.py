# Here is a function that checks if a number is prime
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


# Here is a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]


# Here is filter with lambda to select only prime numbers
prime_numbers = list(filter(lambda number: is_prime(number), numbers))


# Here is the result
print("Prime numbers:", prime_numbers)