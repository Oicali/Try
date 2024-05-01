import math

Fm = float(input("\nEnter magnetic force (in Newtons): "))
q = float(input("Enter electric charge (in Coulumb): "))
v = float(input("Enter velocity (in m/s): "))
angle = int(input("Enter angle (in degrees): "))

convertion = (angle * (math.pi / 180))
angle_Sin = (math.sin(convertion))
magneticField = (Fm / (q * (v * math.sin(convertion))))

print("\nTest 1" + str(convertion))
print("\nTest 2" + str(angle_Sin))
print("\nTHIS IS THE ANSWER: " + str(magneticField))
