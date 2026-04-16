import math

x = 99856;
# result = math.pi;
# result = math.e;
# result = math.sqrt(99856)
# result = math.ceil(x/3)
result = math.floor(x/3)

print(result)

# Exercise 1
radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius;
area = math.pi * (pow(radius,2))

print(f"The circumference of this circle is {round(circumference,3)}")
print(f"The area of this circle is {round(area,3)}cm^2")

#exercise 2, calculating hypotenuse of a right angled triangle

a = float(input("Enter side A of triangle: "))
b = float(input("Enter side B of triangle: "))
c = math.sqrt(pow(a,2)+pow(b,2))

print(f"hypotenuse of this rectangle is {round(c,2)} cm(s)")








