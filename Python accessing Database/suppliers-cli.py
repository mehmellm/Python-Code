import pymysql
import getpass
import os
import sys
import traceback
import os.path

connection = None
connected = False

def tryToConnect():
	global connection,connected,username,pw,schema
	username = input("Enter username: ")
	if username == "*":
		if not os.path.isfile("confile"):
			print("******ERROR  No saved connection in a file named 'confile'*****")
			return
		with open("confile") as f:
			text = f.read()
			lines = text.split("\n")
			if len(lines) != 3:
				print("******ERROR  File 'confile' does not have 3 lines*****")
				return
			username = lines[0]
			schema = lines[1]
			pw = lines[2]
	else:
		schema = input("Enter schema (db): ")
		pw = getpass.getpass("Enter password: ")
		#pw = input("Enter password: ")
	try:
		connection = pymysql.connect(host='brahe.canisius.edu', port=3306, user=username, passwd=pw, db=schema)
		connected = True
		with open("confile", "w") as f:
			f.write(username + "\n" + schema + "\n" + pw)
	except:
		print("****FAILED****")
		sys.exit(1)

def makeNewRecord():
     if not connected:
          print("You must connect first!")
          return

     cur = connection.cursor()

     query_string = "insert into suppliers value(" +   \
                 "'" + input("id number:") + "', " + \
                 "'" + input("name:") + "', " + \
                 input("status:") + ", " + \
                 "'" + input("city where based:") + "'" + \
                 ")"

     n = cur.execute(query_string)
     toshow = query_string + "\n"
     if n == 0:
           toshow += "\n***FAILED!***"
     else:
           toshow += "\nsucceeded"
     print(toshow)

     cur.close()

def change():
     if not connected:
          print("You must connect first!")
          return

     print("Changing...")
     sid = input("id number:")
     curs = connection.cursor()
     numrows = curs.execute("SELECT * from suppliers where sno ='" + sid + "'")
     if numrows == 0:
          print("No such supplier!")
          return

     for row in curs:
          oldname = row[1]
          oldstatus = row[2]
          oldcity = row[3]
          print("oldname="+oldname)

     newname = input("name(" + oldname + "): ")
     if len(newname) == 0:
          newname = oldname
     elif newname == "QUIT":
          return

     newstatus = input("status(" + str(oldstatus) + "): ")
     if len(newstatus) == 0:
          newstatus = str(oldstatus)
     elif newstatus == "QUIT":
          return

     newcity = input("city(" + oldcity + "): ")
     if len(newcity) == 0:
          newcity = oldcity
     elif newcity == "QUIT":
          return

     query_string = "update suppliers set " +   \
                 "sname='" + newname + "', " + \
                 "status=" + newstatus + ", " + \
                 "city='" + newcity + "' " + \
                 "where sno='" + sid + "'"

     cur = connection.cursor()
     n = cur.execute(query_string)

     toshow = query_string + "\n"
     if n == 0:
           toshow += "\n***FAILED!***"
     else:
           toshow += "\nsucceeded"
     print(toshow)

     cur.close()

def delete():
     if not connected:
          print("You must connect first!")
          return

     print("Deleting...")
     sid = input("id number:")
     curs = connection.cursor()
     numrows = curs.execute("SELECT * from suppliers where sno ='" + sid + "'")
     if numrows == 0:
          print("No such supplier!")
          return

     query_string = "delete from suppliers " +   \
                 "where sno='" + sid + "'"
     cur = connection.cursor()
     n = cur.execute(query_string)

     toshow = query_string + "\n"
     if n == 0:
           toshow += "\n***FAILED!***"
     else:
           toshow += "\nsucceeded"
     print(toshow)

     cur.close()


def find():
     if not connected:
          print(" You must connect first!")
          return

     id = input("What is the supplier number? ")
     curs = connection.cursor()
     numrows = curs.execute("SELECT * from suppliers where sno ='" + id + "'")
     if numrows == 0:
          print("Nothing found!")
          return
     prettyPrint(curs)

def printTable():
     if not connected:
          print(" You must connect first!")
          return

     curs = connection.cursor()
     numrows = curs.execute("SELECT * from suppliers order by sno")
     if numrows == 0:
          print("Empty table!")
          return
     prettyPrint(curs)

def prettyPrint(curs):
     s = ""
     for row in curs:
         line = ""
         line = "%-3s %-15s %-3s %-20s" % row
         s += line + "\n"
     print("------------------------------------------------------------")
     print(s)
     print("------------------------------------------------------------")
          

def getMenuChoice():
	print("---- suppliers table ----")
	print("0.  quit")
	print("1.  connect")
	print("2.  find a supplier")
	print("3.  add a new supplier")
	print("4.  change a supplier")
	print("5.  delete a supplier")
	print("6.  print entire table")
	if connected:
		print("    (You are connected as '" + username + "' and to database '" + schema + "')")
	else:
		print("    (You are not connected)")
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
				if connection != None:
					connection.close()
				sys.exit(1)
			if choice == 1:
				tryToConnect()
			elif choice == 2:
				find()
			elif choice == 3:
				makeNewRecord()
			elif choice == 4:
				change()
			elif choice == 5:
				delete()
			elif choice == 6:
				printTable()
			else:
				print("****Illegal choice****")
		except Exception as e:
			crash_msg = str(e)
			tb = traceback.format_exc()
			print("Crashed!  ",crash_msg)
			print(tb)

main()
