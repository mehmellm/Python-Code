'''
   Author: Jacob Mineo, Lucas Mehmel
   Course: CSC 112 lab
   program: BST.py
   Purpose: This is a binary search tree.
'''

from stack import *

class BST:
	def __init__(self):
		self.root = None
		self.debug = False

	def attach(self, value, key):
		if self.root == None:
			self.root = TreeNode(value, key)
			if self.debug:
				print("Just made a new node and made it the tree's root, value=",value,"key=",key)
			return self.root
		else:
			return BST.attach_aux(self.root, value, key)

	def attach_aux(currentNode, value, key):
		if value == currentNode.payload:
			if key not in currentNode.keylist:
				currentNode.keylist.append(key)
			return currentNode
		elif value < currentNode.payload:
			if currentNode.left == None:
				currentNode.left = TreeNode(value, key)
				return currentNode.left
			else:
				return BST.attach_aux(currentNode.left, value, key)
		elif value > currentNode.payload:
			if currentNode.right == None:
				currentNode.right = TreeNode(value, key)
				return currentNode.right
			else:
				return BST.attach_aux(currentNode.right, value, key)

	def prettyPrint(self):
		BST.prettyPrint_aux(self.root, 0)

	def prettyPrint_aux(someNode, indent):
		if someNode == None: return
		BST.prettyPrint_aux(someNode.right, indent+5)
		print(" "*indent, end="")
		print(someNode.payload)
		BST.prettyPrint_aux(someNode.left, indent+5)

	#---------------------------------------stuff below is for students to complete and write ---------------------------

	def find(self, targetvalue):
		return BST.find_aux(self.root, targetvalue)

	def find_aux(someNode, targetvalue):
		if someNode.payload == targetvalue:
			return someNode
		else:
			if someNode.payload < targetvalue:
				return BST.find_aux(someNode.right, targetvalue)
			else:
				return BST.find_aux(someNode.left, targetvalue)
		

	def size(self):
		return BST.size_aux(self.root)

	def size_aux(someNode):
		if someNode == None:
			return 0
		return 1 + BST.size_aux(someNode.left) + BST.size_aux(someNode.right)


	#-------------------------------------students replace the function below with a recursive version--------------------------------
	def makeList2(self):
                return BST.makeList2_aux(self.root)
	def makeList2_aux(someNode):
		if someNode == None:
			return []
		else:
			return BST.makeList2_aux(someNode.left) + [someNode.payload] + BST.makeList2_aux(someNode.right)
		
			
		
#---------------------------------do not change stuff below--------------------------------------------------

class TreeNode:
	def __init__(self, payload, key):
		self.payload = payload
		self.keylist = [key]
		self.left = None
		self.right = None
'''
if __name__ == "__main__":
	tree = BST()
	tree.attach("cat", "July")
	tree.attach("bird", "Charlie")
	tree.attach("cat", "Shelly")
	tree.attach("dog", "Abraham")
	tree.attach("iguana", "Daniel")
	tree.attach("cat", "Yolanda")
	tree.prettyPrint()

	print ("Tried to find cat: ", tree.find("cat").keylist)

	print("Size of tree is",tree.size())
	print("makelist returned: ",tree.makeList2())
'''
