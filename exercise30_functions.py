#functions with positional arguments

def happy_birthday(name, age):
    print(f"Happy Birthday {name}")
    print(f"You are {age} years old")
    print("You are new")
    print()

# happy_birthday("bro", 0)
# happy_birthday("nishant",1.5)
# happy_birthday("faisal","chuddu")

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"You have a bill of {amount:.2f} dollars is due on{due_date}")

# display_invoice("brocode",42.52,"01/01")

def add (x,y):
    return x+y

def subtract (x,y):
    return x-y

def multiply (x,y):
    return x*y

def divide (x,y):
    return x/y

# print(divide(10,2))
# print(add(10,2))
# print(subtract(10,2))
# print(multiply(10,2))

def create_name(first, last):
    first=first.capitalize()
    last=last.capitalize()
    return f"{first} {last}"

print(create_name("bablu", "pandey"))

