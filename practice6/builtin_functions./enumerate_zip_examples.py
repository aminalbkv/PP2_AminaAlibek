students = ["Anna", "Tom", "Alex"]

for index, name in enumerate(students, start=1):
    print(index, name)




names = ["Anna", "Tom", "Alex"]
ages = [18, 19, 20]

for name, age in zip(names, ages):
    print(name, age)