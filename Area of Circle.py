# Area of Circle Program

from cmath import pi
import time

radius = float(input("Enter a Radius: "))

if radius == str:
    print("Enter a valid radius.")

if radius == bool:
    print("Enter a valid radius.")

result = (round(pi * radius * radius, 3))

print("Calculating area of the circle...")
time.sleep(2)


print(f"Area of Circle: {result}")

