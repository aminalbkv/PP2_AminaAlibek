import re

text = input("Enter a string: ")

if re.fullmatch(r"ab*", text):
    print("Match")
else:
    print("No match")