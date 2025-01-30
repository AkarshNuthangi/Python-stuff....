# Force Calculator
# F = m * a

print("Welcome to the Force Calculator!")
mass_input = float(input("Enter mass: "))
acceleration_input = float(input("Enter acceleration: "))

if mass_input == str:
    print("Invalid mass input.")
if mass_input == bool:
    print("Invalid mass input.")

if acceleration_input == str:
    print("Invalid acceleration input.")
if acceleration_input == bool:
    print("Invalid acceleration input.")    


force = (round(mass_input * acceleration_input, 3))

print(f"The force(N) is: {force} N")



