print("Welcome to the Table Generator!!")

a = float(input("Enter the number you want as a table: "))
b = float(input("Enter Number of Multiples: "))
i = 1

while i<=b:
    print(int(a), '*' , int(i), '=', int(a*i))
    i+=1
