from pathlib import Path

folder = Path(__file__).parent

source = folder / "source.txt"
destination = folder / "destination.txt"

source.write_text("Hello, this is Python Practice 6!")

with open(source, "r") as file:
    content = file.read()

with open(destination, "w") as file:
    file.write(content)

print("File copied successfully!")