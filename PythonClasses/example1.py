# Example 1: Class, Object, __init__ and self

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")


# Create objects
student1 = Student("Amina", 18)
student2 = Student("Ali", 19)

student1.introduce()
student2.introduce()