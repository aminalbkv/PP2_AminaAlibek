# Multiple Inheritance

# First parent class
class Student:
    def study(self):
        print("I am studying")


# Second parent class
class Athlete:
    def train(self):
        print("I am training")


# Child class inherits from two classes
class Person(Student, Athlete):
    pass


# Create object
person1 = Person()

# Method from Student
person1.study()

# Method from Athlete
person1.train()