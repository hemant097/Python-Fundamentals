fruits = ["apple","orange","banana","coconut"]
misc = ["celery","carrots","potatoes"]
meat = ["chicken","fish","turkey"]

groceries = [fruits,misc,meat]

# print(groceries[0])
# print(groceries[1][2])

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()

num_pad = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
    ("*",0,"#")
)

for row in num_pad:
    for val in row:
        print(val,end=" ")
    print()
