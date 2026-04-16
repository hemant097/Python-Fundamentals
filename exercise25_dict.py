#dictionary - a collection of {key:value} pairs,
# ordered and changeable. NO DUPLICATES

capitals = {
    "USA":"WASHINGTON D.C.",
    "INDIA":"NEW DELHI",
    "CHINA":"BEIJING",
    "RUSSIA":"MOSCOW"
}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("INDIA"))

# if(capitals.get("JAPAN")):
#     print("that captital exists")
# else:
#     print("not exist")

#adding a new key value pair
# capitals.update({"Germany":"Berlin"})

#updating a kvp
# capitals.update({"INDIA":"New Delhi"})

#removes specified key and returns the value
# print(capitals.pop("RUSSIA"))

#removes the last inserted item, and returns the kvp in the form of 2-tuple
# print(capitals.popitem())

# capitals.clear()

# keys = capitals.keys() #Return a set-like object providing a view on the dict's keys.
# print(keys)
# for key in keys:
#     print(key)

# values = capitals.values() #Return an object providing a view on the dict's values.
# print(values)
# for value in values:
#     print(value)

items = capitals.items() #Return a set-like object providing a view on the dict's items.
print(items)
for key, value in items:
    print(f"{key} -> {value}")

print(capitals)