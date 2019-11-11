# program: getbirthyear2.py
# written by Lucas Mehmel


import datetime
current=(datetime.datetime.now().year)
age = int(input("What is your age? "))
birth_year=(current-age)
print("you were born in",birth_year,"or maybe",(birth_year-1))

