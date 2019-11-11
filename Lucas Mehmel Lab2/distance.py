'''
	Program:  distance.py
	Written by:  Dr. Meyer
	Purpose: To calculate the Euclidean distance between two 2d points on a plane
	How to use:  Run this from the command line and answer the prompts
		When asked for point1, type in something like  3,5.6  or  7,0
		Input: Two lines, two numbers on each line separated by a comma
	Output:  a float that represents the Euclidean distance between the points
'''

import math

point1 = input("Enter point 1 as two numbers separated by a comma:")
x1 = float(point1.split(",")[0])
y1 = float(point1.split(",")[1])

point2 = input("Enter point 2 as two numbers separated by a comma:")
x2 = float(point2.split(",")[0])
y2 = float(point2.split(",")[1])

distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print("The distance from (",point1,") to (",point2,") is ",distance," units", sep = "")
print("The distance from (",point1,") to (",point2,") is ",distance," units")
# print("The distance from (",point1,") to (",point2,") is ",("%.2f" % distance)," units", sep = "")

