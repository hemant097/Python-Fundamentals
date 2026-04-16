# if elif else in python

# weight = float(input("enter your weight: "))
# unit = input("Kilograms or pounds? (K or L): ")
#
# if unit=="K":
#     weight*= 2.205;
#     unit = "Lbs."
#     print(f"The weight is {round(weight, 1)} {unit}")
# elif unit=="L":
#     weight/= 2.205
#     unit = "Kgs."
#     print(f"The weight is {round(weight, 1)} {unit}")
# else:
#     print(f"unit {unit} is not valid")

tempUnit = input("is the temp in Celsis or Fahrenheit, enter C / F : ")
temp = float(input("enter temperature: "));

# Alt+0176 for this degree sign °
if tempUnit=="C":
    temp = round( (9*temp)/5 + 32 , 1)
    print(f"The temp is {temp} °F")
elif tempUnit=="F":
    temp = round((temp-32)*5/9,1)
    print(f"The temp is {temp} °C")
else:
    print(f"This unit {tempUnit} is invalid")


