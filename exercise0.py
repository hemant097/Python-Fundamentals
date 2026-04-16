# this is my first python program
print("I like Aubrey Plaza!");

#Strings str
first_name = "Bro";
food = "burger"
email="bro123@fake.com"
print(food)
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")
print(food[2])

#Integers int
age=25
print(f"You are {age} years old")

#float
price=10.99
print(f"The price of parle-g is {price}")

#boolean (True or False) bool

is_student = True;
print(f"Are you a student:{is_student}")

#if / else

if(is_student):
    print("You are a student")
else:
    print("You are not a student")

for_sale=False;
if for_sale:
    print(f"This item is for sale")
else:
    print(f"This item is not for sale")

# Type casting , process of converting a variable from one data type to another
name="Hemu"
age=26
gpa=3.2
is_person=True

print(type(age))

age=float(age)
print(age)

print(int(gpa))

print(str(age))
print(type(str(age)))

name= bool(name) #type casting string to boolean
print(name)  #will print true
# if the name were an empty string i.e., "", then it will print False, can be used to check if the user has entered their name or not

# input() = to take input
#all the input is received in the form of string, so we have to typecast it later

# input("What is your name?:")
# here we aren't doing anything with input

myName= input("What is your name?:")
myAge = int(input("How old are you?:")) #directly accepting int as input
myAge+=1
print(f"Hello {myName}, hope you are doing well")
print(f"You are {myAge} years old")