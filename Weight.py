#W=mg(where g = 9.8m/s2 on Earth)
#WEIGHT CALCULATOR

user_input = input("Enter Mass: ")
Weight = (round(user_input * 9.8, 3))

if user_input == float or int:
    pass
else:
    print("Error! Invalid Mass Input....")

print(Weight)