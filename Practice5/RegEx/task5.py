import re

text = input("Enter a string: ")

if re.fullmatch(r"a.*b", text):
    print("Match")
else:
    print("No match")