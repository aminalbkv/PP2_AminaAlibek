import re

text = input("Enter a string: ")

if re.fullmatch(r"ab{2,3}", text):
    print("Match")
else:
    print("No match")