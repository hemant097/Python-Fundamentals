# Inheritance allows a class to inherit attributes and methods from another class.
#   Helps with code reusability and extensibility
#     Syntax -   class child(Parent)
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

doggie = Dog("Courage")
cattie = Cat("Garfield")
mouse = Mouse("Stuart")

print(doggie.name)
print(doggie.is_alive)
doggie.eat()
doggie.sleep()
doggie.speak()