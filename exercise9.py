# conditional expression (like ternary operator in other languages)
# X if condition else Y

number=4

print("Postive" if number > 0 else "Negative")
result = "EVEN" if number%2==0 else "ODD"

print(result)

a = 6
b=5

max_num = a if a>b else b
min_num = a if a<b else b
print(max_num)
print(min_num)

user_role = "ADMIN"
access_level = "Full access" if user_role == "ADMIN" else "Limited access"
print(access_level)