def PrintBoard(board):
	boardstr = ""
	linestr = ""
	cnt = 1
	for i in range(63,-1,-1):
		if(board[i]==0):
			if(cnt%2!=0):
				if(i%2==0):
					linestr += "__ "
				else:
					linestr += "## "
			else:
				if(i%2==0):
					linestr += "## "
				else:
					linestr += "__ " 
		else:
			linestr += (str(board[i]) + " ")
		if(i%8==0):
			#linestr += " \n"
			if(i==0):
				linestr = "   " + linestr + "   " + ("%2s" % str((cnt-8)*-8)) + "\n" + "\n" 
				#linestr = ("%2s" % str((cnt-8)*-8))+ "   " + linestr + "\n" + "\n"
				coords= "  " + "  7" + "  6" + "  5" + "  4" + "  3" + "  2" + "  1" + "  0" + "	 "
				#coords= "	 " + "0  " + "1  " + "2  " + "3  " + "4  " + "5  " + "6  " + "7  "
				linestr += coords
			else:
				linestr =  "   " + linestr + "   " + ("%2s" % str((cnt-8)*-8)) + "\n" + "\n"
				#linestr = ("%2s" % str((cnt-8)*-8))+ "   " + linestr + "\n" + "\n"
			boardstr += linestr
			#print(linestr)
			linestr = ""
			cnt += 1
	print(boardstr)
	print("\n")
	print("_ black, # white, 20 offset black, 10 offset white")
	return 0

# def PrintBoard(board):
#	 accum="---- BLACK SIDE ----\n"
#	 max=63
#	 for j in range(0,8,1):
#		 for i in range(max-j*8,max-j*8-8,-1):
#			 accum=accum+'{0: <5}'.format(board[i])
#		 accum=accum+"\n"
#	 accum=accum+"---- WHITE SIDE ----"
#	 print(accum)
#	 return accum

def GenBoard():
	board = [13,11,12,15,14,12,11,13,10,10,10,10,10,10,10,10]
	for i in range(16,48,1):
		board += [0]
	board += [20,20,20,20,20,20,20,20,23,21,22,25,24,22,21,23]
	# print(board)
	return board

def GetPlayerPositions(board, player):
	positions = []
	for i in range(0,64,1):
		if((board[i]-player)>=0 and (board[i]-player)<=5):
			positions += [i]
	return positions
		
def GetPieceLegalMoves(board,position):
	#find which team the piece at the position belongs to
	#determine which board positions are under threat by other team
	#positions not under threat and available for the type of piece are legal moves
	piece = board[position]
	if piece==0:
		print("there is no piece in that position! GetPieceLegalMoves failed.")
		return [-1]
	pieces = {
		10: WPawnLM,
		11: WKnightLM,
		12: WBishopLM,
		13: WRookLM,
		14: WQueenLM,
		15: WKingLM,
		20: BPawnLM,
		21: BKnightLM,
		22: BBishopLM,
		23: BRookLM,
		24: BQueenLM,
		25: BKingLM
	}
	return pieces[piece](board,position)

def WPawnLM(board, position):
	moves=[]
	#starting two square jump
	if(position<=15 and board[position+16]==0):
		moves+= [position+16]

	#next square
	if(position<56 and board[position+8]==0):
		moves += [position +8]
	
	#diagonal squares
	if(position<56 and position%8!=0 and (position-position//8)%7!=0):
		if(board[position+7]>=20):
			moves+=[position+7]
		if(board[position+9]>=20):
			moves+=[position+9]
	elif(position<56 and position%8==0):
		if(board[position+9]>=20):
			moves+=[position+9]
	elif(position<56 and (position-position//8)%7==0):
		if(board[position+7]>=20):
			moves+=[position+7]
	return moves

def BPawnLM(board,position):
	moves=[]
	#starting two square jump
	if(position>=48 and board[position-16]==0):
		moves+= [position-16]

	#next square
	if(position>7 and board[position-8]==0):
		moves += [position-8]	

	#diagonal squares
	if(position>7 and position%8!=0 and (position-position//8)%7!=0):
		if(board[position-7]<16 and board[position-7]>0):
			moves+=[position-7]
		if(board[position-9]<16 and board[position-9]>0):
			moves+=[position-9]
	elif(position>7 and position%8==0):
		if(board[position-7]<16 and board[position-7]>0):
			moves+=[position-7]
	elif(position>7 and (position-position//8)%7==0):
		if(board[position-9]<16 and board[position-9]>0):
			moves+=[position-9]
	return moves

def WKnightLM(board,position):
	moves=[]
	a = []
	if(((position+1)-(position+1)//8)%7==0):
		#cannot do -6 and +10, can do all others
		a=[-10,-17,6,15,17,-15]
	elif((position-1)%8==0):
		#cannot do +6 and -10, can do all others
		a=[-17,15,17,10,-6,-15]
	elif(position%8==0):
		a=[17,10,-6,-15]
	elif((position-position//8)%7==0):
		a=[-10,-17,6,15]
	else:
		a=[-10,-17,6,15,17,10,-6,-15]
	for p in a:
			if((position+p)>=0 and (position+p)<64):
				if(board[position+p]==0 or board[position+p]>15):
					moves+=[position+p]
	return moves

#instead of %7, it should be (position - position//8)%7
def BKnightLM(board,position):
	moves=[]
	a = []
	if(((position+1)-(position+1)//8)%7==0):
		#cannot do -6 and +10, can do all others
		a=[-10,-17,6,15,17,-15]
	elif((position-1)%8==0):
		#cannot do +6 and -10, can do all others
		a=[-17,15,17,10,-6,-15]
	elif(position%8==0):
		a=[17,10,-6,-15]
	elif((position-position//8)%7==0 or (position-position//8)%7==0):
		a=[-10,-17,6,15]
	else:
		a=[-10,-17,6,15,17,10,-6,-15]
	for p in a:
		if((position+p)>=0 and (position+p)<64):
			if(board[position+p]==0 or board[position+p]<=15):
				moves+=[position+p]
	return moves

def WBishopLM(board,position):
	moves=[]
	tmp=position
	while((tmp+7)>=0 and (tmp+7)<64 and tmp%8!=0):
		if(board[tmp+7]==0):
			moves+=[tmp+7]
			tmp+=7
		elif(board[tmp+7]>15):
			moves+=[tmp+7]
			break
		else:
			break
	tmp=position
	while((tmp+9)>=0 and (tmp+9)<64 and ((tmp+1)%8)!=0):
		if(board[tmp+9]==0):
			moves+=[tmp+9]
			tmp+=9
		elif(board[tmp+9]>15):
			moves+=[tmp+9]
			break
		else:
			break
	tmp=position
	while((tmp-7)>=0 and (tmp-7)<64 and ((tmp+1)%8)!=0):
		if(board[tmp-7]==0):
			moves+=[tmp-7]
			tmp-=7
		elif(board[tmp-7]>15):
			moves+=[tmp-7]
			break
		else:
			break
	tmp=position
	while((tmp-9)>=0 and (tmp-9)<64 and tmp%8!=0):
		if(board[tmp-9]==0):
			moves+=[tmp-9]
			tmp-=9
		elif(board[tmp-9]>15):
			moves+=[tmp-9]
			break
		else:
			break
	return moves

def BBishopLM(board,position):
	moves=[]
	tmp=position
	while((tmp+7)>=0 and (tmp+7)<64 and tmp%8!=0):
		if(board[tmp+7]==0):
			moves+=[tmp+7]
			tmp+=7
		elif(board[tmp+7]<=15):
			moves+=[tmp+7]
			break
		else:
			break
	tmp=position
	while((tmp+9)>=0 and (tmp+9)<64 and ((tmp+1)%8)!=0):
		if(board[tmp+9]==0):
			moves+=[tmp+9]
			tmp+=9
		elif(board[tmp+9]<=15):
			moves+=[tmp+9]
			break
		else:
			break
	tmp=position
	while((tmp-7)>=0 and (tmp-7)<64 and ((tmp+1)%8)!=0):
		if(board[tmp-7]==0):
			moves+=[tmp-7]
			tmp-=7
		elif(board[tmp-7]<=15):
			moves+=[tmp-7]
			break
		else:
			break
	tmp=position
	while((tmp-9)>=0 and (tmp-9)<64 and tmp%8!=0):
		if(board[tmp-9]==0):
			moves+=[tmp-9]
			tmp-=9
		elif(board[tmp-9]<=15):
			moves+=[tmp-9]
			break
		else:
			break
	return moves

def WRookLM(board,position):
	moves=[]
	tmp=position
	while((tmp+8)>0 and (tmp+8)<64):
		if(board[tmp+8]==0):
			moves+=[tmp+8]
			tmp+=8
		elif(board[tmp+8]>15):
			moves+=[tmp+8]
			break
		else:
			break
	tmp=position
	while((tmp-8)>0 and (tmp-8)<64):
		if(board[tmp-8]==0):
			moves+=[tmp-8]
			tmp-=8
		elif(board[tmp-8]>15):
			moves+=[tmp-8]
			break
		else:
			break
	tmp=position
	while((tmp+1)<64):
		if((tmp+1)%8==0):
			break
		elif(board[tmp+1]==0):
			moves+=[tmp+1]
			tmp+=1
		elif(board[tmp+1]>15):
			moves+=[tmp+1]
			break
		else:
			break
	tmp=position
	while((tmp-1)>=0):
		if(tmp%8==0):
			break
		elif(board[tmp-1]==0):
			moves+=[tmp-1]
			tmp-=1
		elif(board[tmp-1]>15):
			moves+=[tmp-1]
			break
		else:
			break		
	return moves

def BRookLM(board,position):
	moves=[]
	tmp=position
	while((tmp+8)>0 and (tmp+8)<64):
		if(board[tmp+8]==0):
			moves+=[tmp+8]
			tmp+=8
		elif(board[tmp+8]<=15):
			moves+=[tmp+8]
			break
		else:
			break
	tmp=position
	while((tmp-8)>0 and (tmp-8)<64):
		if(board[tmp-8]==0):
			moves+=[tmp-8]
			tmp-=8
		elif(board[tmp-8]<=15):
			moves+=[tmp-8]
			break
		else:
			break
	tmp=position
	while((tmp+1)>0 and (tmp+1)<64):
		if((tmp+1)%8==0):
			break
		if(board[tmp+1]==0):
			moves+=[tmp+1]
			tmp+=1
		elif(board[tmp+1]<=15):
			moves+=[tmp+1]
			break
		else:
			break
	tmp=position
	while((tmp-1)>0 and (tmp-1)<64):
		if(tmp%8==0):
			break
		if(board[tmp-1]==0):
			moves+=[tmp-1]
			tmp-=1
		elif(board[tmp-1]<=15):
			moves+=[tmp-1]
			break
		else:
			break
	return moves

def WQueenLM(board,position):
	moves=[]
	moves += WRookLM(board,position)
	moves += WBishopLM(board,position)
	return moves

def BQueenLM(board,position):
	moves=[]
	moves += BRookLM(board,position)
	moves += BBishopLM(board,position)
	return moves

def WKingLM(board,position):
	moves=[]
	if(position%8==0):
		a=[1,8,9,-7,-8]
	elif((position+1)%8==0):
		a=[-1,7,8,-9,-8]
	else:
		a = [-1,1,7,8,9,-7,-8,-9]
	for i in a:
		if((position+i)>=0 and (position+i)<64):
			if(board[position+i]==0):
				moves+=[position+i]
			elif(board[position+i]>15):
				moves+=[position+i]
	return moves

def BKingLM(board,position):
	moves=[]
	if(position%8==0):
		a=[1,8,9,-7,-8]
	elif((position+1)%8==0):
		a=[-1,7,8,-9,-8]
	else:
		a = [-1,1,7,8,9,-7,-8,-9]
	for i in a:
		if((position+i)>=0 and (position+i)<64):
			if(board[position+i]==0):
				moves+=[position+i]
			elif(board[position+i]<=15):
				moves+=[position+i]
	return moves

def isCheckmate(board,player):
	for i in range(0,64,1):
		if(board[i]-player==5):
			[underThreat,threats]=IsPositionUnderThreat(board,i,player)
			if(underThreat==True):
				if len(threats)>1:
					kingMoves=GetPieceLegalMoves(board,i)
					for k in kingMoves:
						tmpb=board[:]
						tmpb[k]=tmpb[i]
						tmpb[i]=0
						[newPosThreat,newThreats]=IsPositionUnderThreat(tmpb,k,player)
						if(newPosThreat==False):
							return False
					return True
				elif len(threats)==1:
					kingMoves=GetPieceLegalMoves(board,i)
					for k in kingMoves:
						tmpb=board[:]
						tmpb[k]=tmpb[i]
						tmpb[i]=0
						[newPosThreat,newThreats]=IsPositionUnderThreat(tmpb,k,player)
						if(newPosThreat==False):
							return False
					for l in GetPlayerPositions(board,player):
						if(l!=i):
							pieceMoves=GetPieceLegalMoves(board,l)
							for k in pieceMoves:
								tmpb=board[:]
								tmpb[k]=tmpb[l]
								tmpb[l]=0
								[reCheckThreat,reThreats]=IsPositionUnderThreat(tmpb,i,player)
								if(reCheckThreat==False):
									return False
					return True
				else:
					return False
			else:
				return False
	return False


def isInCheck(board,player):
	for i in range(0,64,1):
		if((board[i]-player)==5):
			[underThreat,threats]=IsPositionUnderThreat(board,i,player)
			return underThreat
	return False

def IsPositionUnderThreat(board,position,player):
	threats=[]
	potentThreats=[]
	piece=board[position]
	underThreat=False
	if(player==10):
		for i in range(0,64,1):
			if((board[i]-10)>=10):
				potentThreats=GetPieceLegalMoves(board,i)
				for k in potentThreats:
					if(position==k):
						threats+=[i]
						underThreat=True
						break
	elif(player==20):
		for i in range(0,64,1):
			if((board[i]-10)<10 and (board[i]-10)>=0):
				potentThreats=GetPieceLegalMoves(board,i)
				for k in potentThreats:
					if(position==k):
						threats+=[i]
						underThreat=True
						break
	return [underThreat,threats]




