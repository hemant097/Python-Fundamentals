# module = a file containing code we might want to include in our program. Using 'import' we can can
# include a module (built-in or custom). Useful to break up in a large program resuable separate files

import math
# import math as mt
# from math import e

# print(math.pi)
# print(mt.pi)
# print(math.e)

a,b,c,d,e = 1,2,3,4,5

#direct import using from can sometimes lead to ambiguity. Thus math.e should be used explicitly
print(math.e**a)
print(math.e**b)
print(math.e**c)
print(math.e**d)
print(math.e**e)

import exercise38_module_example as example

print(example.pi)
print(example.square(3))
print(example.cube(4))
print(example.area(7))
print(example.circumference(5))

