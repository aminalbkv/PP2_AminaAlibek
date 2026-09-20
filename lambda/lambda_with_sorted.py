# Lambda with sorted()
# Sort students by their age

students = [
    ("Amina", 18),
    ("Alex", 20),
    ("Sara", 17)
]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)