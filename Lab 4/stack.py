# -----------------------------------------students do not change this file!---------------------------------

class Stack:
	def __init__(self):
		self.innerlist = []
	
	def isEmpty(self):
		return self.innerlist == []

	def push(self, item):
		self.innerlist.append(item)

	def pop(self):
		thing = self.innerlist[-1]
		del self.innerlist[-1]
		return thing

	def top(self):
		return self.innerlist[-1]