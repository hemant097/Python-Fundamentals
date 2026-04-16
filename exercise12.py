# indexing in string
# [start:end:step]
# start → where to begin (default = start of string)
# stop → where to end (default = end of string)
# step → how to move between characters

credit_card = "1234-5678-9012-3456";

print(credit_card[1])
print(credit_card[0:4]) #end is exclusive
print(credit_card[:4]) #assumes start from zero
print(credit_card[5:9])
print(credit_card[10:]) #assumes end is last

#using negative indexing
print(credit_card[-1])

#using step , here will print every second character, :: assumes from start to end
print(credit_card[::2])

#starting from -4 and end at last
last_four_digits = credit_card[-4:]
print(f"XXXX-XXXX-XXXX-{last_four_digits}")

name = "tnameh"
# prints the entire string in reverse (meaning it interprets as move backwards -1 position each time)
print(name[::-1])

# This does not work, as assumes forward direction, thus can't traverse in -ve direction
namm2 = "babchamo"
print(namm2[5:1])

#This works as we are giving it direction also
 # it interprets as start at index 5 move backward and stop before index 1
namm2 = "babchamo"
print(namm2[5:1:-1])