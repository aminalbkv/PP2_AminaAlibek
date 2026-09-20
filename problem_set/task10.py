# Here is a function that returns unique elements
def unique_elements(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


# Here is an example
numbers = [1, 2, 2, 3, 4, 4, 5]

print(unique_elements(numbers))