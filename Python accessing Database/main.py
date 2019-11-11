import os
import sys
import os.path


def getMenuChoice():
	print("********** MAIN SHELL ***********")
	print("0.  quit")
	print("1.  suppliers")
	temp = input("? ")
	if len(temp) == 0:
		print("****Illegal choice****")
		return -1
	try:
		return int(temp)
	except:
		print("****Illegal choice****")
		return -1

def main():
	while True:
		try:
			choice = getMenuChoice()
			if choice == 0:
				sys.exit(1)
			if choice == 1:
				os.system("python suppliers-cli.py")
				sys.exit(1)
			else:
				print("****Illegal choice****")
		except Exception as e:
			crash_msg = str(e)
			tb = traceback.format_exc()
			print("Crashed!  ",crash_msg)
			print(tb)

main()