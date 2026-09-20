# Example 1: Positional arguments
# The order of arguments is important

def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info("Amina", 18)


# Example 2: Default argument
# If no country is given, Kazakhstan will be used

def student_country(name, country="Kazakhstan"):
    print(name, "is from", country)

student_country("Amina")
student_country("John", "USA")