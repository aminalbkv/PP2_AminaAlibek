# Here is the parent class
class Shape:

    # Here is a method that prints the default area
    def area(self):
        print(0)


# Here is the child class Square
class Square(Shape):

    # Here is a constructor that saves the length
    def __init__(self, length):
        self.length = length

    # Here is a method that calculates the square area
    def area(self):
        print(self.length * self.length)


# Here is an object of the Shape class
shape = Shape()

# Here is an object of the Square class
square = Square(5)

# Here is the area of the default shape
shape.area()

# Here is the area of the square
square.area()