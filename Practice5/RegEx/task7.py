import re

text = input("Enter snake_case: ")

def change(match):
    return match.group(1).upper()

result = re.sub(r"_([a-z])", change, text)

print(result)