# 1. Squares up to N
def square_generator(n):
    for i in range(n + 1):
        yield i * i

n = int(input("Enter N for task 1: "))

for x in square_generator(n):
    print(x)


# 2. Even numbers from 0 to n
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n for task 2: "))

print(*even_generator(n), sep=",")


# 3. Numbers divisible by 3 and 4
def divisible_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n for task 3: "))

for x in divisible_generator(n):
    print(x)


# 4. Squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for x in squares(a, b):
    print(x)


# 5. Numbers from n down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter n for task 5: "))

for x in countdown(n):
    print(x)