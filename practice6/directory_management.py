#Create Nested Directories
import os

os.makedirs("students/python", exist_ok=True)

print("Folders created successfully!")

#List Files and Folders
import os

files = os.listdir("students")

print(files)

#Find Files by Extension
import os

for file in os.listdir("."):
    if file.endswith(".txt"):
        print(file)

#Move and Copy Files
import os
import shutil

os.makedirs("backup", exist_ok=True)

shutil.copy("hello.txt", "backup/hello.txt")

print("File copied successfully!")



os.makedirs("moved_files", exist_ok=True)

shutil.move("backup/hello.txt", "moved_files/hello.txt")

print("File moved successfully!")