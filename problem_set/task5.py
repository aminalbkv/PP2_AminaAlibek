from itertools import permutations


# Here is a function that prints all permutations
def print_permutations(text):
    all_permutations = permutations(text)

    for permutation in all_permutations:
        print("".join(permutation))


# Here is user input
user_text = input("Enter a string: ")

# Here is the function call
print_permutations(user_text)