'''
Author: Lucas Mehmel
Program: superparser.py
Course: CSC 112L
Due Date: May 2, 2017
'''
class Stack():
	def __init__(self):
		''' init, has no parameter, sets up a list which will contain the item  '''
		self.mylist = []

	def push(self, ch):
		'''  returns nothing  '''
		#assert type(ch) is str, "Parameter must be a str"
		self.mylist.append(ch)

	def pop(self):
		'''  returns top thing and removes it from the list '''
		temp = self.mylist[-1]
		self.mylist = self.mylist[:len(self.mylist)-1]
		return temp
	def top(self):
		''' returns top thing but does not remove it '''
		return self.mylist[-1]

	def isEmpty(self):
		''' returns bool, True if len of list is 0, False otherwise '''
		if len(self.mylist) == 0:
			return True
		return False

	def depth(self):
		''' returns int, how many items are in the stack '''
		return len(self.mylist)

	def view(self):
		''' returns a list of all items in the stack, used for debugging '''
		newlist = []
		for i in range(len(self.mylist)):
			newlist += i
		return newlist
