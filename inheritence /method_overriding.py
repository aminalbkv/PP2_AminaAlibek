# Method Overriding

# Parent class
class Person:
    def introduce(self):
        print("Hello, I am a person")


# Child class
class Student(Person):

    # Override the parent method
    def introduce(self):
        print("Hello, I am a student")


person1 = Person()
student1 = Student()

person1.introduce()
student1.introduce()