# Decorator - a function that extends the behaviour of another function w/o modifying the base function
#             Pass the base function as an argument to the decorator
#  @property, @<property>.setter, @staticmethod, @classmethod are some built-in decorator methods

def add_sprinkles(func):
    def wrapper():
        print('** Adding sprinkles...🎊 **')
        func()
        print("** Hope you like your ice-cream with the sprinkles ")
    return wrapper


# if we do not add the wrapper method, we will end up calling get_ice_cream(), as soon as we apply the decorator
#  ,and we don't want such behaviour,
#  Thus wrapper ensures, that only add_sprinkles() when get_ice_cream is called

@add_sprinkles
def get_ice_cream():
    print("Here is your Ice cream 🍧🍨")

# The above line is equivalent to
#                   get_ice_cream = add_sprinkles(get_ice_cream)
# that means, first add_sprinkles first line get printed
#             , second get_ice_cream is called
#             , third add_sprinkles third line gets printed


# we only want sprinkles, when we want ice cream, not whenever we apply the decorator
get_ice_cream()

#now if we are passing any argument in function, we'll get TypeError, to avoid this we need to pass *args, **kwargs

def add_banana(func):
    def wrapper(*args, **kwargs):
        print('** Adding banana...🍌🍌 **')
        func(*args, **kwargs)
    return wrapper

def add_whipped_cream(func):
    def wrapper(*args, **kwargs):
        print('** Adding whipped cream...🍦🍦 **')
        func(*args, **kwargs)
    return wrapper

@add_banana
@add_whipped_cream #we can use more than one decorator
def get_waffle(flavor):
    print(f"Here is your {flavor} waffle 🧇🧇")

print()
get_waffle("red velvet")