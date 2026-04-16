#keyword arguments - an argument preceded by an identifier
#                   helps with readability
#                   order of arguments does not matter


def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")

#positional arguments
hello("Good evening","Mr","Tony","Stark")
#order of arguments does matter
hello("Good evening","Stark","Tony","Mr")

#here order does not matter (But positional argument should be before if we are mixing these)
hello("Hello",title="Mr.",last="Stark",first="Tony")

#this will give error
# hello(title="Mr.",last="Stark",first="Tony","Hello")

for x in range(1,11):
    print(x,end=" ") #here end is a keyword argument

print()
print("1","2","3","4","5","6","7","8", sep="-") #sep is also keyword argument

def get_phone(country_code, area_code, first, last):
    return f"{country_code}-{area_code}-{first}-{last}"

phone_num = get_phone(country_code=91, area_code=123, first=9532, last=6755)
print(phone_num)