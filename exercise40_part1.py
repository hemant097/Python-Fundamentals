# import exercise40_part2

# __name__ within that file will return its own name i.e. __main__,
# but if we are printing __name__ in another file, and importing the file, like in this case we will se two lines as output
# OUTPUT :
#       exercise40_part2
#       __main__
# print(__name__)

def favorite_color(color):
    print(f"Your favorite color is {color}")


def main():
    print("This is exercise4-_part1")
    favorite_color("blue")
    print("Goodbye")

if __name__ == "__main__":
    main()