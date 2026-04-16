
#Polymorphism - There are 2 ways to achieve this
            # 1. Inheritance - An object could be treated of the same type as a parent class
            # 2. "Duck Typing" - in exercise 51

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
     def __init__(self,radius):
         self.radius = radius

     def area(self):
         return self.radius * self.radius*3.14


class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side **2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height*0.5

#if pizza doesn't inherit Circle we get AttributeError, stating 'Pizza' has no attribute 'area'
class Pizza(Circle): #pizza inherits Circle which inherits shape, thus Pizza is also a shape, and fits into shapes[]
    def __init__(self,topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4),Square(5),Triangle(4,5),Pizza("Pepperoni",7)]

for shape in shapes:
    print(f" {shape.__class__.__name__} has area {shape.area()} cm² ")
