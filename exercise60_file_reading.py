import json, csv

# Within the context of a string \ are escape sequences for special character. Use \\ or /
file_path = "C:/Users/hem78/Desktop/input.txt"

print("********** Reading a JSON file **********\n")
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError: #changed the security permission in windows
    print("You do not have permission to access this file")

print("\n********** Reading a JSON file **********\n")
json_file_path = "C:/Users/hem78/Desktop/input.json"

try:
    with open(json_file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content['name']) #printing using key of dict
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You do not have permission to access this file")

print("\n********** Reading a CSV file **********\n")
csv_file_path = "C:/Users/hem78/Desktop/input.csv"

try:
    with open(csv_file_path, "r") as file:
        content = csv.reader(file)
        for row in content:
            print(row)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You do not have permission to access this file")