# This is a Try and Catch System
try:
    x = float(input("X: "))
    y = float(input("Y: "))

except:
    print("Invalid Input")
    exit()

print(f"X + Y = { x + y } ")
