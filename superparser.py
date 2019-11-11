'''
Author: Lucas Mehmel
Program: superparser.py
Course: CSC 112L
Due Date: May 2, 2017
'''

from stack import *

class SuperParser:
	'''
	This class parses a string into nested lists by looking for parentheses. 
	'''
	def __init__(self, raw=""):
		'''
		Initializes the SuperParser.  If the user supplies a string, then it is parsed and put into the
		instance variable self.mylist.  An example of a legal input is  
			(i have (an old cat) and (a ((dog) name= "Ruff Barker"))
		Note that this uses parentheses instead of square brackets and strings do not have quotes around
		them unless there are blanks in the string like "Ruff Barker".  The double quotes are not stored
		by the parser, though the embedded blanks are.
		'''
		if len(raw) > 0:
			self.parse(raw)
		else:
			self.mylist = []    # this is the only instance variable

	def parse(self, raw):
		'''
		Take in a string and break it into a list of tokens.  The list may contain other lists.
		A token is a string like a name, but may contain blanks.  Call on tokenize() first
		to tokenize, then use a stack to descend into sublists.
		This sets the instance variable self.mylist.
		'''
		
		#print("I am in parse ahahah")
		#print("raw= ", raw)
		raw = SuperParser.tokenize(raw)
		#print("raw after SuperParser.tokenize(raw)= ", raw)
		stack = Stack()
		currentlist = []
		for x in raw:
			#print("x= ", x)
			if x == "(":
				stack.push(currentlist)
				currentlist = []
			elif x == ")":
				if stack.isEmpty():
					print("Error.... Stack is empty!!")
					break
				oldcurrentlist = currentlist
				#print("oldcurrentlist: ", oldcurrentlist)
				currentlist = stack.pop()
				currentlist.append(oldcurrentlist)
			else:
				#print("Appending to currentlist")
				currentlist.append(x)
		if stack.isEmpty() == False:
			print("Stack is not empty. Malformed parentheses.")
		#print("returning self.mylist= ", self.mylist)
		self.mylist = currentlist[0]
		
		#print("returning self.mylist= ", self.mylist)

	def tokenize(raw):
		'''
		Take in a string like '(i have a (furry cat) whose name is "luke the duke")'
		and break into a big single level list of strings.  Each left paren and each right paren
		is a separate string.  Each word is a string, and any sequence between double quotes
		is a separate string.  The above turns in:
		["(", "i", "have", "a", "(", "furry", "cat", ")", "whose", "name", "is", "luke the duke", ")"]
		Notice that double quotes are removed from the final string, so you don't see
				""luke the duke""
		When almost done, replace all chr(160) with a true blank.
		'''
		string = SuperParser.replace_blanks_in_strings(raw)
		string = string.replace('"', '')
		string = string.replace("(", "( ")
		string = string.replace(")", " )")
		string = string.replace("  ", " ")
		string = string.replace("  ", " ")
		string = string.replace("  ", " ")
		rawlist = string.split(" ")
		rawlist = [x.replace(chr(160), chr(32)) for x in rawlist]
		#print(rawlist)
		return rawlist
		
			   

	def replace_blanks_in_strings(raw):
		'''
		Because we want to break up the raw string into tokens on a single blank, any interior blanks
		as in "luke the duke" will confuse this.  So replace blanks with chr(160).  This is a special
		kind of blank that prints as a blank but isn't truly a blank, hence the split(" ") method won't
		get confused and will treat "luke the duke" as one big string, because those 'blanks' between
		'e' and 't' and between 'e' and 'd' aren't truly blanks, but the special chr(160).
		'''
		string = ""
		inString = False
		for word in raw:
			if word == '"':
				inString = not inString
			if inString == True:
				if word == ' ':
					string += chr(160)
				else:
					string += word
			else:
				string += word
		string = string.replace('"','')
			
		return string
			      
		

	def flatten(self):
		'''
		Uses a stack to flatten out all nested lists into one big single-level list of words.
		For instance ["i", "have", ["a", "furry", "cat"], "who", [["i"]],"feed"] will turn into
		["i", "have", "a", "furry", "cat", "who", "i", "feed"]
		'''
		return SuperParser.flatten_aux(self.mylist)

	def flatten_aux(somelist):
		'''
		This is the recursive helper function that does the real work of flatten()
		'''
		retlist = []
		for item in somelist:
			if type(item) is list:
				retlist += SuperParser.flatten_aux(item)
			else:
				retlist += [item]
		return retlist

	def flatten2(self):
		''' Create a new stack, set currentlist to a copy of the list you are passing in
		    set return list to the empty list, keep going (until you return inside here):
		    if the current list is not empty then, get the first thing in the current list and save it in a variable,
		    let's call it item, delete that first thing off the list
		    if that item is not a list then just append it to the return list
		    otherwise, push the current list onto the stack,
		    set current list to that item because that's what you will now be flattening into the return list
		    otherwise, if the stack is empty, you're done so return the return list
		    otherwise, pop the stack and that thing you just popped becomes the current list'''
		stack = Stack()
		currentlist = self.mylist
		returnlist = []
		i = 0
		while True:
			if i >= len(currentlist):
				if stack.isEmpty():
					break
				i, currentlist = stack.pop()
			elif type(currentlist[i]) is list:
				stack.push((i + 1, currentlist))
				currentlist = currentlist[i]
				i = 0
			else:
				returnlist += [currentlist[i]]
				i += 1
		return returnlist

	def display(self):
		'''
		Uses a stack to print the nested self.mylist vertically.  (Students! do not change this)
		'''
		stack = Stack()
		print(self.mylist)
		currentlist = self.mylist
		#print(currentlist)
		indent = "\t"
		i = 0
		while True:
			if i >= len(currentlist):
				indent = indent[1:]
				if stack.isEmpty():
					break
				i, currentlist = stack.pop()
				#print("Just popped, i=",i,"  currentlist=",currentlist)
				print("")
			elif type(currentlist[i]) is list:
				stack.push((i+1,currentlist))
				#print("Pushed ",stack.top())
				currentlist = currentlist[i]
				i=0
				indent += "\t"
			else:
				print(indent,currentlist[i],sep="")
				i += 1

	def search(self, target):
		'''
		Try to find a word in the nested self.mylist.  Calls on the recursive search_aux()
		for the real work.  Since that recursive method does not need to see or change any
		instance variables, it is a class method.
		(Students!  Do not change this)
		'''
		print("Searching for",target)
		if not SuperParser.search_aux(self.mylist, target):
			print("Not found!")

	def search_aux(somelist, target):
		'''
		Recursive method to find a string in the list "somelist" (which starts out as self.mylist
		but will be inner sublists of this as it recurses.)  Use a for loop to walk through
		somelist, but when you see a nested list, call search_aux on it.
		If you find the target in somelist, use one_level_display() to print it out and return True.
		If you don't find it, either in somelist or in any nested list within somelist, return False.

		This is a class method; no instance variables are used.
		'''
		#print(somelist)
		for item in somelist:
			if type(item) is list:
				if SuperParser.search_aux(item,target):
					return True
			if target == item:
				#print(SuperParser.one_level_display(somelist))
				return True
		return False
	

	def one_level_display(somelist):
		'''
		Given a list named somelist, return a string where the brackets turn into parentheses.
		Also, if there are nested sublists within somelist, display them as "(...)" and do not
		show their contents.
		For example, if somelist is ["i", "love", ["my", "black", "cat"], "mightily"]
		then this will return "(i love (...) mightily)"
		Notice that double quotes do not appear around the strings.

		This is not a recursive method.
		'''
		
		string = "("
		for item in somelist:
			if type(item) is list:
				string += " (...) "
			else:
				if item == " ":
					item = "\"" + item + "\""
				string += item + " "
		string += ")"
		return string

'''
if __name__ == "__main__":
	test = "(cat (eat food) (in bathroom area \"in his litterbox\" with (the door closed)))"
	sp = SuperParser(test)
	sp.display()
	print("calling flatten2: ", sp.flatten2())
	sp.search("food")
	sp.search("cat")
	sp.search("bathroom")
	sp.search("door")

	test = "(cat (eat food) (in bathroom area \"in his litterbox\" with (the door closed)))"
	sp = SuperParser(test)
	sp.display()

	#test = "(too many(right parens)))"
	#sp = SuperParser(test)

'''
