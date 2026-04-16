import exercise40_part1
from exercise40_part1 import favorite_color


# print(__name__)

# if there is no check in script1, i.e. if __name__ == "__main__", then all the code outside the main function (if ther is a main function)
# will get executed.
# Suppose we remove the check in script 1 and move the code outside the main,
# now if we run this file, all the code from script 1 will get executed too, even though our script 2 is empty
# OUTPUT:
# This is exercise4-_part1
# Your favorite color is blue
# Goodbye

def favoruite_drink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is script2")
    favorite_color("Red") #as the scrip1 has the name==main , we can use this function, without invoking everythin else
    favoruite_drink("Coca-cola")
    print("Goodbye")

# if there is a piece of code in a file, which we only want to work, when run that file directly, we should put that in
# the main() with the below check
if __name__=="__main__":
    main()




