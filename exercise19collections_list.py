# List  = [] ordered and changeable, Duplicates OK
# Set = {} unordered and immutable, Add/remove OK, Duplicates NOT OK
# Tuple = () ordered and unchangeable, Duplicates OK, FASTER

#List

fruits = ["apple", "banana", "cherry","mango","pineapple"]

# print(fruits)
# print(fruits[2])
# print(fruits[0:2]) #prints index 0,1
# print(fruits[:3]) # prints index 0,1,2
# print(fruits[::2]) # prints every second elements starting from 0
# print(fruits[::-1]) #prints in reverse

# for fruit in fruits:
#     print(fruit)

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))

# print("mango" in fruits) #returns a bool
# print("kiwi" in fruits)

#mutable list
# fruits[0]="pineapple"
# print(fruits)

#Clear by name
fruits.append("orange")
print(fruits)

fruits.remove("pineapple")
print(fruits)

fruits.insert(0,"taroi")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(fruits.index("orange"))

fruits.append("banana")
print(fruits.count("banana"))

fruits.clear()
print(fruits)