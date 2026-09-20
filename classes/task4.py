import math


# Here is a class for a point
class Point:

    # Here is a constructor that saves x and y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Here is a method that shows the coordinates
    def show(self):
        print("Point:", self.x, self.y)

    # Here is a method that changes the coordinates
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    # Here is a method that calculates the distance between two points
    def dist(self, other_point):
        distance = math.sqrt(
            (self.x - other_point.x) ** 2 +
            (self.y - other_point.y) ** 2
        )
        return distance


# Here are two Point objects
point1 = Point(1, 2)
point2 = Point(4, 6)

# Here are the original coordinates
point1.show()
point2.show()

# Here is the distance between two points
print("Distance:", point1.dist(point2))

# Here is a change of point1 coordinates
point1.move(3, 4)

# Here are the new coordinates
point1.show()