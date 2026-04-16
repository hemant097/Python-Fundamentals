# logical operators in python
# or
# and
# not

temp = 0
is_raining = False

if temp>35 or temp<0 or is_raining:
    print("the event is cancelled")
else:
    print("Party is ONN baby")

is_sunny=False

if temp>=28 and is_sunny:
    print("Perfect weather")
elif temp<=0 and is_sunny:
    print("It is cold outside")
elif 0<temp<28 and is_sunny:
    print("warm weather ")
elif temp>=28 and not is_sunny:
    print("cloudy")
elif temp<=0 and not is_sunny:
    print("It is chilling")
elif 28> temp >0 and not is_sunny:
    print("it is still cold ")