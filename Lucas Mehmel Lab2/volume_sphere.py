'''
    Program: volume_sphere.py
    Written by: Lucas Mehmel
    Purpose: write a program that calculates the volume of a sphere
    


'''
import math
d = int(input("diameter:\n"))
r = d/2
v = 4/3*math.pi*r**3
print(v)
