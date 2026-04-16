# Set = {} unordered and immutable, Add/remove OK, Duplicates NOT OK

fruits = {"apple", "banana", "cherry","mango"}

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)

fruits.add("pineapple")
print(fruits)
fruits.remove("pineapple")

fruits.remove("apple")
print(fruits)

print(fruits.pop()) #it's random as set in unordered

fruits.clear()