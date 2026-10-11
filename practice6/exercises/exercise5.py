from pathlib import Path

fruits = ["Apple", "Banana", "Orange", "Mango"]

path = Path(__file__).parent / "fruits.txt"

with open(path, "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

print("List written successfully!")