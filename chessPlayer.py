from chess2 import *
from gametree import *
from mima import *
import time
import random

# def getTime():
#	 h=True
#	 while(h):
#		 if(time.process_time()>10):
#			 h=False
#	 print(time.process_time())

#Minimax player
def chessPlayer(board,player):
	startTime=time.time()
	gametree=GameTree(board,0,-1,-1,2)
	gametree.populateTree(gametree,player,4)
	mm=MiniMax(gametree)
	# ab=AlphaBeta(gametree)
	#Search for and return best move
	best=mm.minimaxSearch(mm.gametree,player)
	# best=ab.abSearch(ab.gametree,player)
	if(best==None):
		print("Black choosing randomly")
		acc=[]
		positions=GetPlayerPositions(board,player)
		for i in positions:
			moves=GetPieceLegalMoves(board,i)
			if len(moves)>0:
				for k in moves:
					[threat,threats]=IsPositionUnderThreat(board,k,player)
					if threat==False:
						acc+=[[i,k]]
		move=acc[random.randint(0,len(acc)-1)]
		candidateMoves=GetPieceLegalMoves(board,move[0])
		endTime=time.time()
		print("TIMEITIMEITIME")
		print("Time taken to move: " + str(endTime-startTime))
		return [True,move,candidateMoves,None]
	else:
		endTime=time.time()
		print("TIMEITIMEITIME")
		print("Time taken to move: " + str(endTime-startTime))
		return [True,best.getMove(),best.getCandMoves(),best.getLevelOrder()]
	












