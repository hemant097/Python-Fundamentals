# @property - Decorator used to define a method as a property (it can be accessed like an atrribute)]
#             Benefit - Add additional logic when read, write, or delete attributes
#             Gives you setter, getter , and deleter method

class Rectangle:
    def __init__(self, width, height):
        #prepending with _ declares it as a protected member
        self._width = width
        self._height = height

    def __str__(self):
        return (f"W - {self._width} cm, H - {self._height} cm")

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter
    def width(self, new_width):
        if(new_width <= 0):
            print("width must be greater than 0")
        else:
            self._width = new_width

    @height.setter
    def height(self, new_height):
        if(new_height <= 0):
            print("height must be greater than 0")
        else:
            self._height = new_height

    @width.deleter
    def width(self):
        del self._width
        print("width deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height deleted")



rect = Rectangle(100, 200)

#using getter
print(rect.width)
print(rect.height)

#using setter
rect.width = 55
rect.height = 55

print(rect)

#using deleter

del rect.width
del rect.height

# will give error now, as it's been deleted
print(rect.width)