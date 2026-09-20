# Lambda with map()
# Multiply every number in the list by 2

numbers = [1, 2, 3, 4, 5]

doubled_numbers = list(map(lambda x: x * 2, numbers))

print(doubled_numbers)