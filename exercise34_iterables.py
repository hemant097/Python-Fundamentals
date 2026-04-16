# Iterables - an object/collection that can return its elements one at a time,
# allowing to be iterated over in a loop


numbers=[1,2,3,4,5]

#List is iterable
for num in numbers:
    print(num)


#Tuples are also iterable
tnumbers = (1,2,3,4,5)
for num in tnumbers:
    print(num, end="|")

#Set
print()
fruits={"apple","orange","banana","mango"}
for fruit in fruits:
    print(fruit,end=",")

#set not reversible
# for fruit in reversed(fruits):
#     print(fruit,end=",")

#String
name="bablu babylon"

print()
for letter in name:
    print(letter,end=",")

#Dictionary

my_dict = {
    "A":1, "B":2, "C":3, "D":4, "E":5
}

#by default dictionary iterates over keys, OR we can also use .keys() method
print()
for key in my_dict:
    print(key)

#we can iterate our values if required using .values()
print()
for value in my_dict.values():
    print(value)

#we can iterate over both when required using .items()
print()
for key,value in my_dict.items():
    print(f"{key} -> {value}")





