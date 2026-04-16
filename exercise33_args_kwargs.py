# *args - allows you to pass multiple non-key arguments
# **kwargs - allows you to pass multiple keyword-arguments
#     * unpacking operator

# *args are interacted with like a tuple
# **kwargs are interacted with like a dict

def add(*nums):
    print(type(nums))
    total = 0
    for num in nums:
        total+=num
    return total

# print(add(1,2,3,4,5))

def display_name(*args):
    for arg in args:
        print(arg,end=" ")
# display_name("steve","rogers","pandey","nanlu")

print()
def print_address(**kwargs):
    print(type(kwargs))

    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="Naubasta",
                    city="CNB",
                    state="UP",
                    zip="208021",
                    country="IN",
                    apartment="B14")

#keyword arguments should follow positional arguments
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()

    if("apartment" in kwargs):
        print(f"{kwargs.get('street')} {kwargs.get('apartment')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.","Spongebob","SquarePants","III",
               street="Naubasta",
                # apartment="B14",
               pobox="po box 123",
               city="CNB",
               state="UP",
               zip="208021")