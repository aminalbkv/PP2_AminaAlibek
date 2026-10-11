from pathlib import Path
import string

folder = Path(__file__).parent / "letters"
folder.mkdir(exist_ok=True)

for letter in string.ascii_uppercase:
    file = folder / f"{letter}.txt"
    file.write_text(f"This is file {letter}")

print("26 files created successfully!")