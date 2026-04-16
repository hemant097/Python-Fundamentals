# Static method = a method that belong to a class rather than any object from that class instance
#                     Usually used for general utility function, that do not need access to class data
# Instance method - Best for operations on instances of the class (objects)

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["manager","cashier","cook","janitor"]
        return position in valid_positions

employee1 = Employee("Nishant", "manager")
employee2 = Employee("Faisal","cashier")
employee3 = Employee("Spongebob","janitor")

#static method called with class
print(Employee.is_valid_position("manager"))

#instance method called with object
print(employee1.get_info())
