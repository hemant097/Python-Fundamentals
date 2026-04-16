# Exception - an event that interrupts the flow of a program

# 1/0 #ZeroDivisionError
# 1+"1" #TypeError
# int("Pizza") #ValueError

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("Cannot divide by zero, you IDIOT")
except ValueError:
    print("Enter only numbers please")
finally :
    print("Completed")