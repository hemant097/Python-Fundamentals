# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB)
#       Local -> Enclosed -> Global -> Built-in

from math import e #built-in
def func1():
    x=13 #Local scope, if there was no x here, both function calls would print same x (global) value
    print(x)

def func2():
    print(x)

x = 45 #global

func1()
func2()

def func3():
    print(e)

e=99 # we are replacing the built-in e value, thus 99 will get printed ( as global is higher in the scope resolution order)
func3()

def outer():
    # x = 101
    def inner():
        # x = 102
        print(x)
    inner()

# if all x are present i.e. local , enclosed, global, then local (102) will get printed
# if local was absent then enclosed(101) gets printed
# if both are absent then global(45) gets printed
outer()