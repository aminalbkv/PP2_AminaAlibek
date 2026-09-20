# Go through numbers from 1 to 10
for number in range(1, 11):

    # Skip number 5
    if number == 5:
        continue

    print(number)

# Create a list of students
students = ["Amina", "Anna", "Alex", "Tom"]

for student in students:

    # Skip Alex
    if student == "Alex":
        continue

    print(student)

# Go through numbers from 1 to 10
for number in range(1, 11):

    # Skip even numbers
    if number % 2 == 0:
        continue

    print(number)