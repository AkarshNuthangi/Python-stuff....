# Python calculator
# You can also use funcs to make this Calculator!

operator = input("Enter an arithmetic operation(+, -, *, /): ")

num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3)) 
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))

else:
    print(f"'{operator}' is not valid.")             


