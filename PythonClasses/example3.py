# Example 3: Modify, add and delete properties

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Amina", 18)

print("Original age:", person1.age)

# Modify property
person1.age = 19

print("New age:", person1.age)

# Add new property
person1.city = "Almaty"

print("City:", person1.city)

# Delete property
del person1.age

print("Age property was deleted")