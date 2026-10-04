import re

text = input("Enter a string: ")

result = re.findall(r"[a-z]+_[a-z]+", text)

print(result)