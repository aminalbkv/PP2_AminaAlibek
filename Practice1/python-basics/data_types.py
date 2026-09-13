# Example 1: Basic data types
name = "Amina"
age = 18
height = 170.5
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


# Example 2: List, tuple, dictionary, set
subjects = ["Python", "Calculus", "Database"]
colors = ("red", "blue", "green")
student = {"name": "Amina", "age": 18}
fruits = {"apple", "banana", "cherry"}

print(type(subjects))
print(type(colors))
print(type(student))
print(type(fruits))


# Example 3: None type
result = None

print(result)
print(type(result))


# Example 4: Converting data types
x = "20"

print(type(x))

x = int(x)

print(type(x))
print(x + 5)


# Example 5: Difference between text and number
a = "10"
b = "20"

print(a + b)

x = 10
y = 20

print(x + y)