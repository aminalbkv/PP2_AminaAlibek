with open("hello.txt", "w") as file:
    file.write("Hello, Python!")

with open("hello.txt", "r") as file:
    print(file.read())

with open("hello.txt", "a") as file:
    file.write("\nI love Python!")

with open("hello.txt", "r") as file:
    print(file.read())


import shutil

shutil.copy("hello.txt", "backup.txt")

print("File copied successfully!")


import os

if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("File deleted successfully!")
else:
    print("File does not exist!")