# Example 2: Class variable vs Instance variable

class Student:

    # Class variable
    university = "KBTU"

    def __init__(self, name, major):
        # Instance variables
        self.name = name
        self.major = major


student1 = Student("Amina", "IT Management")
student2 = Student("Ali", "Computer Science")

print(student1.name, student1.major, student1.university)
print(student2.name, student2.major, student2.university)