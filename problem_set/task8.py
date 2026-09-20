# Here is a function that checks for 007
def spy_game(numbers):
    code = [0, 0, 7]
    position = 0

    for number in numbers:
        if number == code[position]:
            position += 1

            if position == 3:
                return True

    return False


# Here are examples
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))