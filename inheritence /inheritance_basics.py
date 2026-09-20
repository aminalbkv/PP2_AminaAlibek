# Inheritance Basics

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")


# Child class inherits from Person
class Student(Person):
    pass


# Create an object of Student
student1 = Student("Amina", 18)

# Student can use properties from Person
print(student1.name)
print(student1.age)

# Student can also use methods from Person
student1.introduce()