import re

text = input("Enter camelCase: ")

result = re.sub(r"([A-Z])", r"_\1", text)

print(result.lower())