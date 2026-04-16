# membership operators - used to test whether a value or varinble is found in a sequence
# (string, list, tuple, or dictionary)
#                   1. in
#                   2. not in

#Using string

word="APPLE"
letter = input("Guess a letter in the secret word: ")

#checks whether letter is in word , returns a boolean , not in is just opposite of that
if (letter in word):
    print(f"There is a {letter} in the secret word")
else:
    print("letter not in the word")

#using set

students = { "Spongebob", "Hemant","Sam"}
student = input("Enter the name of the student: ")

if(student in students):
    print(f"{student} is a member of students")
else:
    print("student not in the list")

#using dictionary

grades = {
    "Sandy":"A",
    "Faisal":"B",
    "Ben":"C",
    "Gwen":"D"
}

stud_grade = input("Enter the name of the student: ")
if(stud_grade in grades):
    print(f"{stud_grade}'s grade is {grades[stud_grade]}")
else:
    print(f"{stud_grade}'s grade is not in the list")

#checking valid email
email="hemudon@gmail.com"

if("@" in email and "." in email):
    print(f"{email} is a valid email")
else:
    print(f"{email} is not a valid email")


