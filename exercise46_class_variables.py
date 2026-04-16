#class variables - shared among all instances of the class
                    # defined outside the constructor
                    # Allow you to share data among all objects created from that class

class Student:

#   These 2 are class variables
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Ben Tennyson", 13)
student2 = Student("Gwen Tennyson", 14)

print(student1.name)
print(student1.age)
# print(student1.class_year) #Works but this might look like an instance variable of the class
# print(student2.class_year)
print(Student.class_year) # for better clarity, this is recommended. by looking at this we easily get the idea that this is a class variable

student3 = Student("Chhota Bhim",16)
student4 = Student("Kalia", 17)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)