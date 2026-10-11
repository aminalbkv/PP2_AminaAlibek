import os

path = __file__

if os.path.exists(path):
    print("Path exists!")
    print("Filename:", os.path.basename(path))
    print("Directory:", os.path.dirname(path))
else:
    print("Path does not exist!")