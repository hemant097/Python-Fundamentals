# super() - Function used in a child class to call methods from a parent class (superclass)
#         Allows us to extend the functionality of the inherited methods
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and { 'filled' if self.is_filled else 'unfilled' }.")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) #calling method from superclass
        self.radius = radius


class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height

    #extending the functionality of the inherited method
    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {0.5*self.base*self.height} cm^2")

class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.side**2} cm^2")


# as the color, is_filled attribute was repeating in each class, we create a parent class Shape, of those fields,
# and initialized using super


circle = Circle("red", False, 5)
square = Square("blue", True, 5)
triangle = Triangle("green", False, 5, 10)

print(circle.color)
print(square.is_filled)
print(f"{square.side} cm")

circle.describe() #here this will use Shape describe method
triangle.describe() #this will use Triagle describe method
square.describe()

