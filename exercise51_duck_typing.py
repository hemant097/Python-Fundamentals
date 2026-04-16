# Duck Typing - Another way to achieve polymorphism besides inheritance.
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW MEOW!")

#this class is completely unrelated to Animal, we have make it look like Animal, by creating a speak method.
# So, the loop below will print HONK HONK
#Now if we add the alive attribute also (we won't see AttributeError, as
# we've made Car look like Animal (thus achieved duck typing)

class Car:
    alive = False
    def speak(self):
        print("HONK HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)