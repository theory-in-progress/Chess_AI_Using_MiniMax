#pos good for white
#neg good for black
from chess2 import *
import time

class GameTree:
	def __init__(self,board,score,initPos,finalPos,depth):
		#Value is a 2-list with value[0] being the evaluation and value[1] being the current board array
		self.value=[score,board]
		self.moveToThisBoard=[initPos,finalPos]
		#children is an array of gametrees which are successors
		self.children=[]
		self.candMoves=[]
		self.maxDepth=depth

	def evalBoard(self,board):
		material=0
		numMoves=0
		pawnStruc=0
		checkStatus=0
		#Complete first three heuristics in one for loop
		for i in range(0,64):
			#material
			if(board[i]==10):
				material+=1
			elif(board[i]==11):
				material+=3		
			elif(board[i]==12):
				material+=3  
			elif(board[i]==13):
				material+=5	   
			elif(board[i]==14):
				material+=9		
			elif(board[i]==15):
				material+=100		
			elif(board[i]==20):
				material-=1		
			elif(board[i]==21):
				material-=3		
			elif(board[i]==22):
				material-=3		
			elif(board[i]==23):
				material-=5		
			elif(board[i]==24):
				material-=9		
			elif(board[i]==25):
				material-=100

			#numMoves
			if(board[i]!=0):
				moves=GetPieceLegalMoves(board,i)
				if((board[i]-10)>=10):
					numMoves-=len(moves)
				else:
					numMoves+=len(moves)

			#pawnStruc
			if(board[i]==10):
				if(board[i+7]==10):
					pawnStruc+=1
				if(board[i+9]==10):
					pawnStruc+=1
			elif(board[i]==20):
				if(board[i-7]==20):
					pawnStruc-=1
				if(board[i-9]==20):
					pawnStruc-=1

		#checkStatus
		checkStatus = self.checkStatus(board)
		heuristicSum = material + numMoves/4 + pawnStruc*5 + checkStatus
		return heuristicSum

	def checkStatus(self,board):
		acc=0
		if(isInCheck(board,10)):
			acc-=25
		if(isInCheck(board,20)):
			acc+=25
		if(isCheckmate(board,10)):
			acc-=300
		if(isCheckmate(board,20)):
			acc+=300
		return acc

#populate gametree
#gametree has root value
#find board of gametree
#find positions of player
#find moves for these positions
#for each move, create a child gametree with the board they would form
#add these child gametrees to the root gametree
#repeat for all child gametrees until at max depth

	def populateTree(self,node,player,maxDepth):
		d=0
		start=time.time()
		self.populateTreeHelper(node,player,d,maxDepth,start)
		# print("POP OVER, NODE CHILDREN ARE")
		# print(node.children)
		return True

	def populateTreeHelper(self,node,player,cDepth,maxDepth,start):
		end=time.time()
		if(end-start)>6:
			cDepth=maxDepth
			print("populate time limit reached")
			print(end-start)
		board=node.value[1]
		if(cDepth==maxDepth):
			return True
		else:
			cDepth+=1
			if player==10:
					nextPlayer=20
			else:
				nextPlayer=10
			positions=GetPlayerPositions(board,player)
			for i in positions:
				pMoves=GetPieceLegalMoves(board,i)
				for k in pMoves:
					tmpb=board[:]
					tmpb[k]=tmpb[i]
					tmpb[i]=0
					child=GameTree(tmpb,0,i,k,node.maxDepth-1)
					child.value[0]=child.evalBoard(child.value[1])
					node.candMoves+=[[[i,k],float(child.value[0])]]
					node.children+=[child]
					self.populateTreeHelper(child,nextPlayer,cDepth,maxDepth,start)
		return True

	def getChildren(self):
		return self.children

	def getRoot(self):
		return self.value

	def getMove(self):
		return self.moveToThisBoard

	def getCandMoves(self):
		return self.candMoves

	def getLevelOrder(self):
		d=self.maxDepth
		tarr=[]
		tarr+=[self.value[1]]
		tarr=self.getLevelOrderHelper(self,tarr,d)
		return tarr

	def getLevelOrderHelper(self,tree,tarr,d):
		if d<0:
			return tarr
		d-=1
		for i in tree.getChildren():
			tarr+=[i.value[1]]
			return self.getLevelOrderHelper(i,tarr,d)