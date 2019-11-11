import sys
import random

class Board:
	def __init__(self):
		self.board = []
		for i in range(4):
			self.board.append([' ',' ',' ',' '])
		self.current_player = "X"
		self.numcycles = 0
		self.mode = "normal"
	
	def _set(self,row,col):
		'''
		   puts the current player's symbol into the board at row and col.
		   Row and col range from 0 to 3 inclusive.
		'''
		self.row = row
		self.col = col
		if self.current_player == "X":
			self.board[self.row][self.col] = self.current_player
			self.current_player = "O"
		elif self.current_player == "O":
			self.board[self.row][self.col] = self.current_player
			self.current_player == "X"
		

	def _isEmpty(self,row,col):
		'''
		   returns True if nothing is there yet
		'''
		self.row = row
		self.col = col
		if self.board[self.row][self.col] == " ":
			return True
		return False

	def makeMove(self,row,col):
		'''
		   tries to put the current player's symbol into the board at row and col if empty.
		   Returns True if the place is empty, False if it was occupied.
		'''
		
		self.row = row
		self.col = col
		if self._isEmpty(self.row,self.col) == True:
			self._set(self.row,self.col)
			return True
		else:
			if self.current_player == "X":
				self.current_player = "O"
			return False  

	def clear(self):
		'''
		   returns the board to a cirgin state, ready to start a new game
		'''
		self.board = []
		for i in range(4):
			self.board.append([' ',' ',' ',' '])
		return self.board
			
	    
	def chooseStarter(self):
		self.current_player = "X"
		return "X"

	def setMode(self,mode = "normal"):
		'''
		   sets the mode, based on the parameter
		'''
		self.mode = mode
		

	def _grab(self):
		'''
		   if "spoiler" mode is on, the system randomly picks an unoccupied spot and places"*" there.
		   If it first chooses an occupied spot, it keeps trying again until it finds one.
		   This method is called after one round of plays by two players.
		'''
		ranrow = random.randint(0,3)
		rancol = random.randint(0,3)
		rangrab = random.randint(0,1)
		print(rangrab)
		if rangrab < 5:
			while self.board[ranrow][rancol] != " ":
				ranrow = random.randint(0,3)
				rancol = random.randint(0,3)
			self.board[ranrow][rancol] = "*"  


	def checkForWinner(self):
		'''
		   sees if the board contains a winning configuration for either "X" or "O".
		   If either wins, it returns the symbol of the winner.
		   If neither won it returns a blank.
		'''
		
		self.win = []
		for s in range(4): #first diagnol
			self.win.append(self.board[s][s])
		if self._findWinner(self.win) == "X":
			return "X"
		elif self._findWinner(self.win) == "O":
			return "O"
		
		for s in self.board: # rows
			if self._findWinner(s) == "X":
				return "X"
			elif self._findWinner(s) == "O":
				return "O"
		for s in range(4): # cols
			self.win = []
			for i in range(4):
				self.win.append(self.board[i][s])
			if self._findWinner(self.win) == "X":
				return "X"
			elif self._findWinner(self.win) == "O":
				return "O"
		self.win = []
		for s in range(4): # sencond diagnol
			i = 3
			self.win.append(self.board[s][i-s])
		if self._findWinner(self.win) == "X":
			return "X"
		elif self._findWinner(self.win) == "O":
			return "O"
		else:
			return " "


	def checkIfFull(self):
		'''
		   sees if the board contains no empty spaces. Return True if full.
		'''
		for i in range(4):
			for s in range(4):
                                if self.board[i][s] == " ":
                                        return False
		return True

	def _findWinner(self,onelist):
		'''
		Determines in a winning streak occurs in the list that is the parameter.
		A winning streak is 3 "X" in a row, or 3 "O" in a row.
		If it finds a winner, it returns it.  So it would return "X" or "O", in there is a winning streak.
		If no winner, it returns a blank.
		'''
		self.onelist = onelist
		assert type(self.onelist) is list, "Parameter must be a list of 1-char strings"
		assert len(self.onelist) == 4, "Parameter must be a list of 4 strings"
		for i in range(4):
			assert len(self.onelist[i]) == 1, "Parameter must be a list of four strings, each 1 char long"
			assert self.onelist[i] in " XO*", "Parameter's chars can only be blank, X, O, or * "
			assert type(self.onelist[i]) is str, "Parameter must contain lists of strings"
		temp = "".join(self.onelist)        # squish down to one string
		if "XXX" in temp:
			return "X"
		if "OOO" in temp:
			return "O"
		return " "   # no winner!

	def __str__(self):
		'''
		   returns a string that represents the 4x4 board.
		'''
		return ("o-------o \n"
		       "|" + self.board[0][0] + "|" + self.board[0][1] + "|" + self.board[0][2] + "|" + self.board[0][3] + "| \n"
		       "o-------o \n"
		       "|" + self.board[1][0] + "|" + self.board[1][1] + "|" + self.board[1][2] + "|" + self.board[1][3] + "| \n"
		       "o-------o\n"
		       "|" + self.board[2][0] + "|" + self.board[2][1] + "|" + self.board[2][2] + "|" + self.board[2][3] + "| \n"
		       "o-------o\n"
		       "|" + self.board[3][0] + "|" + self.board[3][1] + "|" + self.board[3][2] + "|" + self.board[3][3] + "| \n"
		       "o-------o")

