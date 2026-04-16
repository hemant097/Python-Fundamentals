
#object - A "bundle" of related attributes (variables) and methods (functions)
#class - blueprint used to desing the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive_car(self):
        print(f"Driving Car {self.model} of color {self.color}")

    def stop_car(self):
        print(f"{self.model} of color {self.color} car is stopped")

    def describe_car(self):
        print(f"{self.model} of color {self.color} of year {self.year} car is described")

car1 = Car("Brezza",2016,"Blue",True)
car2 = Car("Tavera",2004,"Red",True)
car3 = Car("Seltos",2022,"Black",False)



def display_car_details(car):
    print(car.model)
    print(car.year)
    print(car.color)
    print(car.for_sale)
    print("-------------")

display_car_details(car1)
display_car_details(car2)
display_car_details(car3)

car1.drive_car()
car1.stop_car()
car3.describe_car()

