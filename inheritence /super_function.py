# Super Function

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Child class
class Student(Person):
    def __init__(self, name, age, major):

        # Call the parent constructor
        super().__init__(name, age)

        # New property for Student
        self.major = major

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Major:", self.major)


# Create Student object
student1 = Student("Amina", 18, "IT Management")

student1.show_info()