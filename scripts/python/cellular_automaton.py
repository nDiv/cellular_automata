import math
import time

def simAutomaton(n):
	startT = time.time()
	
	lives = 0
	for i in range(1,2**n):
	
		if(simStateGen(num2state(i,n))):
			lives = lives + 1
			currentT = time.time()
			print("Current lives: %d, time: %f" % (lives,currentT-startT))
		
		if(i%1000 == 0):
			currentT = time.time()
			print("Loop: %d, time: %f" % (i,currentT-startT))
	
	endT = time.time()
	print("It took %f seconds" % (endT-startT))
	return lives

def isExtinct(state):
	
	for i in range(len(state)):
		for j in state[i]:
			if(j == 1):
				return False
	return True
	
def nextState(state):
	
	n = len(state)
	nState = [[0]*n for x in range(n)]
	
	for i in range(n):
		for j in range(n):
			nb_sum = sum(neigbhors(state,i,j))
			#print("sum of (%d,%d) is %d" % (i,j,nb_sum))
			if(nb_sum == 1 or nb_sum == 2):
				nState[i][j] = 1
			#else:
				#nState[i][j] = 0
	
	return nState
	
def neigbhors(state,i,j):
	nb = []
	n = len(state)-1 # Largest index of the list.
	if([i,j] == [0,0]): # Top-left corner
		nb_id = [[1,0],[1,1],[0,1]]
		for r in enumerate(nb_id):
			nb.append(state[r[1][0]][r[1][1]])
	elif([i,j] == [0,n]): # Top-right corner
		nb_id = [[0,j-1],[1,j-1],[1,j]]
		for r in enumerate(nb_id):
			nb.append(state[r[1][0]][r[1][1]])
	elif([i,j] == [n,0]): # Bottom-left corner
		nb_id = [[i-1,j],[i-1,j+1],[i,j+1]]
		for r in enumerate(nb_id):
			nb.append(state[r[1][0]][r[1][1]])
	elif([i,j] == [n,n]): # Bottom-right corner
		nb_id = [[i-1,j],[i-1,j-1],[i,j-1]]
		for r in enumerate(nb_id):
			nb.append(state[r[1][0]][r[1][1]])
	else:
		if(i == 0): # Top row
			nb_id = [[0,j-1],[1,j-1],[1,j],[1,j+1],[0,j+1]]
			for r in enumerate(nb_id):
				nb.append(state[r[1][0]][r[1][1]])
		elif(i == n): # Bottom row
			nb_id = [[i,j-1],[i-1,j-1],[i-1,j],[i-1,j+1],[i,j+1]]
			for r in enumerate(nb_id):
				nb.append(state[r[1][0]][r[1][1]])
		elif(j == 0): #Left row
			nb_id = [[i-1,0],[i-1,1],[i,1],[i+1,1],[i+1,0]]
			for r in enumerate(nb_id):
				nb.append(state[r[1][0]][r[1][1]])
		elif(j == n): # Right row
			nb_id = [[i-1,j],[i-1,j-1],[i,j-1],[i+1,j-1],[i+1,j]]
			for r in enumerate(nb_id):
				nb.append(state[r[1][0]][r[1][1]])
		else: # Elsewhere
			nb_id = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
			for r in enumerate(nb_id):
				nb.append(state[r[1][0]][r[1][1]])
	
	return nb
	
def statesEqual(S1,S2):
	
	n = len(S1)
	
	for i in range(n):
		for j in range(n):
			if(S1[i][j] != S2[i][j]):
				return False
	return True
	
def simStateGen(state):
	
	initState = list(state)
	counter = 0
	while(True):
		state = nextState(state)
		if(isExtinct(state)):
			return False
		
		if(statesEqual(state,initState)):
			return True
			
		if(counter > 100):
			break
			
	return -1 #Something wrong happened!
	
def num2state(num, n):
	
	numBits = n**2
	if(num > 2**numBits-1):
		print("%d cannot be represented by %d bits" % (num, numBits))
		return -1
	
	digits = [0]*numBits
	state = [[0]*n for x in range(n)]
	
	count = numBits-1
	i = 0
	j = 0
	index = n-1
	
	while(num > 0):
		digits[count] = num%2
		num = int(math.floor(num/2))
		
		state[i][j] = digits[count]
		j = j + 1
		
		if(j > index):
			j = 0
			i = i + 1
			
		
		count = count - 1
		if(count < 0):
			break
	
	return state

