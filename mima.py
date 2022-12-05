from gametree import *
from chess2 import *

class MiniMax:

	#gametree has root called value - value[0] gives evaluation of board, value[1] gives board
	#gametree has children which are also gametree objects
	def __init__(self,gametree):
		self.gametree=gametree
		self.children=gametree.getChildren()

	def minimaxSearch(self,node,player):
		#Max player goes first
		#Get all eval states recursively
		#if player==20:
		bestVal=self.minTurn(node)
		# else:
		#	 bestVal=self.maxTurn(node)
		#bestVal=self.minTurn(node)
		#print(bestVal)
		bestMove=None
		children=self.getChildren(node)
		for i in children:
			if i.value[0]==bestVal:
				bestMove=i
				break
		return bestMove

	def maxTurn(self,node):
		if(self.atBottom(node)):
			return self.getNodeValue(node)
			
		inf=float('inf')
		maxVal=-inf
		children=self.getChildren(node)
		for i in children:
			maxVal=max(maxVal,self.minTurn(i))
		return maxVal

	def minTurn(self,node):
		if(self.atBottom(node)):
			return self.getNodeValue(node)

		inf=float('inf')
		minVal=inf
		children=self.getChildren(node)
		for i in children:
			minVal=min(minVal,self.maxTurn(i))
		return minVal

	def atBottom(self,node):
		print(node.getChildren())
		if(len(node.getChildren())==0):
			return True
		return False

	def getNodeValue(self,node):
		return node.value[0]

	def getChildren(self,node):
		return node.children