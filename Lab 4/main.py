import SuperDict

mydict = SuperDict.SuperDict()

def make_sample():
	mydict.put("Maddie", "dog")
	mydict.put("Mark", "cat")
	mydict.put("Vladimir", "snake")
	mydict.put("Sally", "cat")
	mydict.put("Kathy", "dog")
	mydict.put("Anthony", "dog")

while True:
	try:
		command = input("Command: ")
		if command == "quit":
			break
		elif command.startswith("debug="):
			if command[6:] == "on":
				mydict.setdebug(True)
			else:
				mydict.setdebug(False)

		#----- add more commands here -----

		elif command.startswith("@"):
			command = command[1:]
			exec(command)
		else:
			pass   # this is the key, just a string.  Look it up in the dictionary
	except Exception as e:
		print("Exception occurred: " + str(e))

		