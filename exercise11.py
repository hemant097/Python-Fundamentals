
username = input("Please enter your username: ")

if( len(username) > 12 ):
    print("Your username is too long.")
elif(username.find(" ") >= 0):
    print("username cannot contain spaces.")
elif(not username.isalpha()):
    print("username contains invalid characters.")
else:
    print(f"Welcome {username}")