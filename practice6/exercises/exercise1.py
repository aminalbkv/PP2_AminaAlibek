from pathlib import Path

path = Path(__file__).parent

directories = []
files = []

for item in path.iterdir():
    if item.is_dir():
        directories.append(item.name)
    elif item.is_file():
        files.append(item.name)

print("Directories:", directories)
print("Files:", files)
print("All:", directories + files)