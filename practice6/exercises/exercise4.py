from pathlib import Path

path = Path(__file__).parent / "sample.txt"

with open(path, "w") as file:
    file.write("Hello\n")
    file.write("Python\n")
    file.write("Practice 6\n")

with open(path, "r") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))