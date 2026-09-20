# Go through numbers from 1 to 10
for number in range(1, 11):

    # Stop the loop when number is 6
    if number == 6:
        break

    print(number)

# Create a list of students
students = ["Anna", "Alex", "Amina", "Tom"]

for student in students:

    # Stop when we find Amina
    if student == "Amina":
        print("Amina found!")
        break

    print(student)

# Create a list of numbers
numbers = [10, 20, 30, 100, 40]

for number in numbers:

    # Stop if the number is 100
    if number == 100:
        break

    print(number)