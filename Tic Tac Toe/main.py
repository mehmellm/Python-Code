from board import *

b = Board()
mode = input("What mode would you like to play?: ")
b.setMode(mode)

while True:
	b.chooseStarter()
	if b.checkIfFull():
		print(b.numcycles, "moves played")
		break
	if b.checkForWinner() == "X":
		print("X IS THE WINNER!!!", "Won in ", b.numcycles, " moves")
		break
	if b.checkForWinner() == "O":
		print("O IS THE WINNER!!!", "Won in ", b.numcycles, " moves")
		break
	x = tuple(input("X make your move: "))
	if b.makeMove(int(x[0])-1, int(x[2])-1) == False:
		print("That spot is taken. Lose turn!!")
	if b.makeMove(int(x[0])-1, int(x[2])-1) == True:
		b.makeMove(int(x[0])-1, int(x[2])-1)
	if b.checkForWinner() == "X":
		print("X IS THE WINNER!!!", "Won in ", b.numcycles, " moves")
		break
	o = tuple(input("O make your move: "))
	if b.makeMove(int(o[0])-1, int(o[2])-1) == False:
		print("That spot is taken. Lose turn!!")
	if b.makeMove(int(o[0])-1, int(o[2])-1) == True:
		b.makeMove(int(o[0])-1, int(o[2])-1)
	if b.checkForWinner() == "O":
		print("O IS THE WINNER!!!", "Won in ", b.numcycles, " moves")
		break
	if b.mode == "spoiler":
		b._grab()
	print(b)
	b.numcycles += 1
