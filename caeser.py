'''
    Program: caeser.py
    Written by: Lucas Mehmel
    Purpose:
    Input:
    Output:

    Algorithm:
          

'''

import math

string = input("Enter a string: ")

password = int(input("Enter a password (0-25): "))

for ch in string:
	if ch != " ":
		n = ord(ch)
		print(chr(((ord(ch)-65 + password) % 26) + 65),end="")
	else:
		print(" ",end="") 


