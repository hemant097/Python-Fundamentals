import csv
import json

txt_data = "I like burger"

file_path = "test_file/exercise59_text_output.txt"

# "w" - will overwrite the file with this text even if it already exists i.e, if it doesn't exist,
#     it creates the file and writes, if it does exist, it replaces the file (i.e., previous content goes away)
# "x" -  will only write in this file, if it doesn't exist i.e., it checks whether the file exists if yes gives error
#   if no, then creates the file and writes it
# "a" - will append the content

# writing text to a file
try:
    with open(file_path, "w") as file:
        file.write(txt_data+"\n")
        print(f"txt file '{file_path}' written")
except FileExistsError:
    print("This file already exists")

employee_names = ["Eugene","Squidward","Ben Tennyson","Gwen TennySon"]

# writing list to a file
try:
    with open(file_path, "a") as file:
        for employee in employee_names:
            file.write(employee+"\n")
        print(f"txt file '{file_path}' written")
except FileExistsError:
    print("This file already exists")

# --------------------------------------------

#creating a nested json like structure
employee = {
    "name":"Carl Jung",
    "age":30,
    "job":"Software Engineer",
    "department":{
        "name":"Core Engineer",
        "Location":"Bengaluru"
    }
}

# writing  json file
file_path = "test_file/exercise59_json_output.txt"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"JSON file created at path '{file_path}' ")
except FileExistsError:
    print("This file already exists")

# ---------------------------------------------------
#writing CSV file
students = [ ["name","age","branch","Address"],
             ["Faisal",29,"IT","Bijnor"],
             ["Nishant",29,"CS","Varanasi"],
             ["Jayendra",29,"CE","Kanpur"]
             ]
file_path = "test_file/exercise59_csv_output.txt"
try:
    with open(file_path, "w",newline="") as file:
        writer = csv.writer(file)
        for row in students:
            writer.writerow(row)
        print(f"CSV file created at path - {file_path}")
except FileExistsError:
    print("This file already exists")