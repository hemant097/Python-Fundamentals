#while loop

#1

# name = input("Enter your name: ")
#
# while (name==""):
#     print("Why didnt you enter ur name")
#     name = input("Enter your name: ")
#
# print(f"Hello {name}")

#2

# age = int(input("Enter your age: "))
#
# while (age<0):
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
#
# print(f"You are {age} years old")

#3

# food = input("What food do you like?, Press q to quit")
#
# while not food == "q" and food.isalpha():
#     print(f"You liked {food}")
#     food = input("What food do you like, Press q to quit")
# print("bye")

#4

num = int(input("Enter a # between 1 and 10: "));

while (num<1 or num>10):
    print(f"{num} is not a valid number. Try again.")
    num = int(input("Enter a # between 1 and 10: "));

print(f"Your number is {num}")
