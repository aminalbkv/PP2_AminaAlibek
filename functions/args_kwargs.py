# Example 1: *args
# *args allows the function to receive any number of positional arguments

def show_subjects(*subjects):
    print("Subjects:", subjects)

show_subjects("Python", "Calculus", "Database")


# Example 2: **kwargs
# **kwargs allows the function to receive any number of keyword arguments

def show_student(**student):
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("City:", student["city"])

show_student(name="Amina", age=18, city="Almaty")