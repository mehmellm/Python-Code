#  program:  prog2.py
#  written by Lucas Mehmel

print("this program translates km to miles or vice versa.")
print("Choose one of the following:")
print("0. quit")      
print("1 km to miles")
print("2. Mileas to km")

choice=int(input("?"))

if choice == 1:
    km = float(input("How many kilometers? "))
    miles = km * 0.621371
    print(km,"km = ",miles,"miles")
elif choice == 2:
    miles = float(input("how many miles? "))
    km = miles / 0.621371
    print(miles,"miles = ",km,"km")
else:
    print("Good-bye")

