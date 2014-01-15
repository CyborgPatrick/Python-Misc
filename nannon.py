from random import randint
import itertools
import sys




class die(object):
	id_iterand = itertools.count(1)
	def __init__(self):
		self.id = self.id_iterand.next()
		self.roll = randint(1,6)


class gameboard(object):
	boardplaces = [ '0' ,'1','2','3','4','5','6','7']
	board = ['X','X','X',' ',' ','O','O','O']
	turn = 0
	moves = []
	xbase = [1,0] 
	obase = [1,0]
	roll = 0


def check_Moves(bord):


	if bord.turn == 1:
		for i in range(8):
			if bord.board[i] == 'X' and i+bord.roll > 6:
				bord.moves.append([i,'O-Base'])
			elif bord.board[i] == 'X' and bord.board[i+bord.roll] == ' ':
				bord.moves.append([i,i+bord.roll])
			elif bord.board[i] == 'X' and bord.board[i+bord.roll] == 'O' and (bord.board[i+bord.roll-1] in (' ','X')) and (bord.board[i+bord.roll+1] in (' ','X')):
				bord.moves.append([i,i+bord.roll])

	if bord.turn == 2:
		for i in reversed(range(8)):
			if bord.board[i] == 'O' and i-bord.roll < 1:
				bord.moves.append([i,'X-Base'])
			elif bord.board[i] == 'O' and bord.board[i-bord.roll] == ' ':
				bord.moves.append([i,i-bord.roll])
			elif bord.board[i] == 'O' and bord.board[i-bord.roll] == 'X' and (bord.board[i-bord.roll-1] in (' ','O')) and (bord.board[i-bord.roll+1] in (' ','O')):
				bord.moves.append([i,i-bord.roll])



def print_Moves(bord):
	print 'You can make the following moves:'

	if bord.turn == 1:
		marker = 'X'
	elif bord.turn == 2:
		marker = 'O'

	for i in range(len(bord.moves)):
		print 'Move ' + str(i+1) + ': move ' + marker +' from ' + str(bord.moves[i][0]) + ' to ' + str(bord.moves[i][1])


def make_Move(bord,choice):
	chosen = bord.moves[int(choice)-1]
	from1 = chosen[0]
	to1 = chosen[1]


	if bord.turn == 1:

		if to1 == 'O-Base':
			bord.obase[1] = bord.obase[1]+1
		else:
			if bord.board[to1] == 'O':
				bord.board[7] = 'O'
				bord.obase[0] = bord.obase[0]+1


			bord.board[to1] = 'X'

		if from1 == 0 and bord.xbase[0]>=1:
			if bord.xbase[0] == 1:
				bord.board[from1] = ' '
			else:
				bord.board[from1] = 'X'
			bord.xbase[0] = bord.xbase[0]-1
		else:
			bord.board[from1] = ' '


	elif bord.turn == 2:
		if to1 == 'X-Base':
			bord.xbase[1] = bord.xbase[1]+1
		else:
			if bord.board[to1] == 'X':
				bord.board[0] = 'X'
				bord.xbase[0] = bord.xbase[0]+1

			bord.board[to1] = 'O'

		if from1 == 7 and bord.obase[0]>=1:
			if bord.obase[0] == 1:
				bord.board[from1] = ' '
			else:
				bord.board[from1] = 'O'
			bord.obase[0] = bord.obase[0]-1
			
		else:
			bord.board[from1] = ' '



def initroll(bord):
	initroll1 = die().roll
	initroll2 = die().roll

	if initroll1 == initroll2:
		initroll(bord)
		return

	print 'Player 1 rolls: ' + str(initroll1)
	print 'Player 2 rolls: ' + str(initroll2)

	

	if initroll1 > initroll2:
		bord.turn = 1
		bord.roll = initroll1-initroll2


	elif initroll1 < initroll2:
		bord.turn = 2
		bord.roll = initroll2-initroll1
		

def BlockHandler(bord):

	print 'No moves available. Passing'

	if bord.turn == 1:
		bord.turn = 2
	elif bord.turn == 2:
		bord.turn = 1

	bord.roll = die().roll
	print 'Player ' + str(bord.turn)+ ' rolled: ' + str(bord.roll) 

	bord.moves = []

	check_Moves(bord)
	if bord.moves == []:
		BlockHandler(bord)
		return
	else:
		print_Moves(bord)


def nannon():

	#Init------

	bord = gameboard()

	initroll(bord)

	print 'Player ' + str(bord.turn)+ ' starts with roll: ' + str(bord.roll) 
	print ''
	print ' '.join(map(str, bord.boardplaces))
	print ' '.join(map(str,bord.board))
	print str(bord.xbase[0])+'             '+str(bord.obase[0])
	print ''
    
	check_Moves(bord)
	print_Moves(bord)
	print ''

	#Init------


	#Main Loop
	while True:

		print ''

		while True:
 			choice =  raw_input('Choose a move (number): ')
 			try:
 				if int(choice)-1 in range(len(bord.moves)): 
 					break
 				else:
 					print 'Wrong input'
 			except:
 				print 'Wrong input'

		make_Move(bord,choice)

		print ''
		
		print ' '.join(map(str, bord.boardplaces))
		print ' '.join(map(str,bord.board))
		print str(bord.xbase[0])+'             '+str(bord.obase[0])
		print ''

		if bord.xbase[1] == 3 or bord.obase[1] == 3:
			print 'Game over'
			if bord.xbase[1] == 3:
				print 'Player 2 Wins!'
			elif bord.obase[1] == 3:
				print 'Player 1 Wins!'
			sys.exit()


		if bord.turn == 1:
			bord.turn = 2
		elif bord.turn == 2:
			bord.turn = 1


		bord.roll = die().roll
		print 'Player ' + str(bord.turn)+ ' rolled: ' + str(bord.roll) 

		#Reset moves list
		bord.moves = []

		#Check for new moves
		check_Moves(bord)

		if bord.moves == []:

			BlockHandler(bord)
			
		else:
			print_Moves(bord)

		print ''


if __name__ == '__main__':
	nannon()
