from chess2 import GenBoard, isInCheck, PrintBoard, GetPieceLegalMoves, isCheckmate
from chessPlayer import *
from gametree import *
import time

#print and generate the board
board = GenBoard()
done=False
while not(done):
	possible=False
	while not(possible):
		checked=isInCheck(board,10)
		print("Board:\n")
		PrintBoard(board)
		print("--------White's Move--------\n")
		#White in check!
		if(checked==True):
			print("You are in check.")
			piece=int(input("Which position would you like to move?\n"))
			if(board[piece]<=15):
				move=int(input("Where would you like to move the piece?\n"))
				candMoves=GetPieceLegalMoves(board,piece)
				for i in candMoves:
					if(move==i):
						tmpb=board[:]
						tmpb[move]=tmpb[piece]
						tmpb[piece]=0
						stillCheck = isInCheck(tmpb,10)
						if(stillCheck==False):
							possible=True
						else:
							print("This move does not relieve you from check. Try again!")
						break
				if(possible):
					board[move]=board[piece]
					board[piece]=0
				elif(possible==False):
					print("That move is not possible.")
			else:
				print("You do not have a piece in that position! \n")
		
		#White not in check!
		else:
			print("Not in check.")
			piece=int(input("Which position would you like to move?\n"))
			if(board[piece]<=15):
				move=int(input("Where would you like to move the piece?\n"))
				candMoves=GetPieceLegalMoves(board,piece)
				for i in candMoves:
					if(move==i):
						tmpb=board[:]
						tmpb[move]=tmpb[piece]
						tmpb[piece]=0
						inCheck = isInCheck(tmpb,10)
						if(inCheck==False):
							possible=True
						else:
							print("This move puts you in check. Try again!")
						break
				if(possible):
					board[move]=board[piece]
					board[piece]=0
				elif(possible==False):
					print("That move is not possible.")
			else:
				print("You do not have a piece in that position! \n")

	# print("CHECKMATE CHECK BEFORE BLACK TURN")
	# print("#########################")
	#Check if last move resulted in black's checkmate
	if(isCheckmate(board,20)):
		print("This is checkmate. White wins!")
		done=True
		break

	# Black is AI
	######## This is random move generation #######
	# movePutsCheck=True
	# while movePutsCheck==True:
	#	 [status,move,candidateMoves]=chessPlayer(board,20)
	#	 tmpb=board[:]
	#	 tmpb[move[1]]=tmpb[move[0]]
	#	 tmpb[move[0]]=0
	#	 movePutsCheck = isInCheck(tmpb,20)
	# board[move[1]]=board[move[0]]
	# board[move[0]]=0
	movePutsCheck=True
	while movePutsCheck==True:
		[status,move,candidateMoves,evalTree]=chessPlayer(board,20)
		tmpb=board[:]
		tmpb[move[1]]=tmpb[move[0]]
		tmpb[move[0]]=0
		movePutsCheck=isInCheck(tmpb,20)
	board[move[1]]=board[move[0]]
	board[move[0]]=0
	print(board)

	# print("CHECKMATE CHECK BEFORE WHITE TURN")
	# print("#########################")
	#Check if last move resulted in black's checkmate
	if(isCheckmate(board,10)):
		print("This is checkmate. Black wins!")
		done=True
		break


# find ./ -type f -exec sed -i 's/\t/	/g' {} \;