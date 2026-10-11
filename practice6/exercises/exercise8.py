import os
from pathlib import Path

folder = Path(__file__).parent
path = folder / "delete_me.txt"

path.write_text("This file will be deleted.")

if os.path.isfile(path):
    if os.access(folder, os.W_OK | os.X_OK):
        os.remove(path)
        print("File deleted successfully!")
    else:
        print("No permission to delete!")
else:
    print("File does not exist!")