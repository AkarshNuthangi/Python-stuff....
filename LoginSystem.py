user_name1 = "Akarsh"
password1 = 'akarsh1234567890'


user_name = input("Enter Username: ")
password = input("Enter Password: ")

if user_name == user_name1:
    print("Username is correct!")
else:
    print("Username is not correct!")  
if password == password1:
    print("Password is correct!")
else:
    print("Password is not correct!")    

if (password and user_name) == (password1 and user_name1):
    print("Logged In Successfully!")
else:
    print("Error!")    