# Here is the parent class
class Shape:

    # Here is a method that prints the default area
    def area(self):
        print(0)


# Here is the child class Rectangle
class Rectangle(Shape):

    # Here is a constructor that saves length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Here is a method that calculates the rectangle area
    def area(self):
        print(self.length * self.width)


# Here is an object of the Rectangle class
rectangle = Rectangle(5, 3)

# Here is the area of the rectangle
rectangle.area()