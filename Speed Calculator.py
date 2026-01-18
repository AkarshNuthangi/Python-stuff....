# Speed Calculator
# Speed = Distance/Time

import time

print("Welcome to the Speed Calculator!")


distance_input = float(input("Enter Distance: "))
time_input = float(input("Enter time(m/s^2): "))

if distance_input == str:
    print("Invalid input.")
if distance_input == bool:
    print("Invaid input.")

if time_input == str:
    print("Invalid input.")
if time_input == bool:
    print("Invalid input.")      

speed = distance_input / time_input

print("Calculating Speed...")
time.sleep(2)

print(f"The speed is: {speed}")

