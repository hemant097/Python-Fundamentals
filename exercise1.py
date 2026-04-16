# Calculate area rectangle with user input

length = float(input("Enter the length"));
width = float(input("Enter the width"));
area = length*width;

# the shortcut to include superscript here is Numlock+alt+0178
print(f"The area is {area}cm²");

x = 3.14
y=-4
z=5

y+=1; #now y is -3
z-=1; # z is 4
z*=2; # z is 8

print(z**2) #square of 8
print(z%2) # remainder when div by 2

print(f"round of x is {round(x)}")
print(f"abs of y is {abs(y)}")
print(f"z raised to power of 3 is {pow(z,3)}")
print(f"max among x,y,z is {max(x,y,z)}")
print(f"min among x,y,z is {min(x,y,z)}")