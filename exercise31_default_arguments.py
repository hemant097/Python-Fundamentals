#default arguments - a default value for certain parameters, can make function more flexible, reduces # of arguments
import time

def net_price( list_price, discount, tax):
    return list_price * (1- discount) * (1+ tax)

print(net_price(100, 0, 0.05))


def net_pricev2( list_price, discount=0, tax=0.05):
    return list_price * (1- discount) * (1+ tax)

print(net_pricev2(500)) #omitted other arguemnts, thus default value is user
print(net_pricev2(500,0.1)) # replaced one argument
print(net_pricev2(500,0.05,0)) # replaced both argument

#default arguments can only come in last
def count(end, start=0):
    for i in range(start, end+1):
        print(i)
        time.sleep(0.1)
    print("DONE")

count(10);

count(25,20)
