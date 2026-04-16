import os
#file detection

def check_file(file_path):
    if os.path.exists(file_path):
        print(f"File exists at {file_path}")

        if os.path.isfile(file_path):
            print("That is a file")
        elif os.path.isdir(file_path):
            print("That is a directory")
    else:
        print(f"File does not exist at {file_path}")

file_path1 = "C:/Users/hem78/Desktop/test"
file_path2 = "C:/Users/hem78/Desktop/Fastreader.txt"
file_path3 = "test_file/exercise58_test.txt"

check_file(file_path1)
check_file(file_path2)
check_file(file_path3)