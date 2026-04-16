# List comprehension = A concise way to create lists in python. Compact and easier to read than traditional loops
#  Syntax = [expression for value in iterable if condition]
doubles=[]

#normal way
#11 is exclusive here,
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

#using list comprehension (like map in java)
triples = [x*3 for x in range(1,11)]
print(triples)

squares = [x**2 for x in range(1,11)]
print(squares)

fruits = ["apple","banana","orange","mango"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)

first_letter_fruits = [ fruit[0] for fruit in uppercase_fruits]
print(first_letter_fruits)

#with conditions  (like filter in java)
numbers=[1,-2,3,-4,5,-6,10,-7]
positive_nums = [ num for num in numbers if num>=0]
negative_nums = [ num for num in numbers if num<0]
even_nums = [num for num in numbers if num%2==0]
odd_nums = [num for num in numbers if num%2!=0]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades = [85,42,79,90,56,61,30]

passing_grades = [ grade for grade in grades if grade>=60]
print(passing_grades)