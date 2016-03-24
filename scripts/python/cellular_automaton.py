import math
import time

def simAutomaton(n):
	"""
	n - size of an nxn grid automaton
	returns lives - the sum of all initial states
					that do not go extinct.
	"""
	startT = time.time()
	
	lives = 0
	noExtinct = []
	numSaved = [0]
	for i in range(1,2**(n*n)): # Loop through all possible states except the zero state.
	
		if(simStateGen(num2state(i,n),noExtinct,numSaved)): # If state does not go extinct, increment lives.
			lives = lives + 1
			#currentT = time.time()
			#print("Current lives: %d, time: %f" % (lives,currentT-startT))
		
		
		if(i%10000 == 0):
			currentT = time.time()
			print("Loop: %d, time: %f seconds" % (i,currentT-startT))
		
	endT = time.time()
	print("It took %f seconds" % (endT-startT))
	print("States saved: %d" % numSaved[0])
	print("States left over: %d" % len(noExtinct))
	return lives

def isExtinct(state):
	"""
	returns True if state is extinct, i.e., the zero state;
	and False otherwise.
	"""
	for i in range(len(state)):
		for j in state[i]:
			if(j == 1):
				return False
	return True
	
def nextState(state):
	"""
	returns the next state given the current state,
	following this rule:
		A cell is alive in the next generation (or state)
		if it has one or two adjacent neighbors that are alive,
		otherwise it's dead.
	"""
	
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
	"""
	returns nb, a list of neighbors of cell (i,j) in state.
	"""
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
	"""
	return True if states S1 and S2 are equal,
	otherwise False
	"""
	
	n = len(S1)
	for i in range(n):
		for j in range(n):
			if(S1[i][j] != S2[i][j]):
				return False
	return True
	
def simStateGen(state,noExtinct,numSaved):
	"""
	returns False if state goes extinct after generations
	and True otherwise.
	The rules applied are:
		(1) A state is extinct if it's equal to the zero state.
		(2) A is not extinct if it either returns to the initial or
			it never reaches the zero state after trying all possible states.
	This rule is inefficient and a more efficient one must be implemented.
	If this state does not go extinct, noExtinct collects intermediate states
	that repeated - showing that it will not go extinct.
	"""
	
	#initState = list(state)
	initNum = state2num(state)
	states = [initNum] # List of states that have occurred, represented by numbers
								# and initialized with the initial state.
	
	if(initNum in noExtinct): # If state has led some state to not go extinct, then state
							  # will not go extinct, too.
		del noExtinct[noExtinct.index(initNum)]
		return True

	n = len(state)
	counter = 0
	while(True):
		state = nextState(state)
		num = state2num(state)
		
		if(sum([i == num for i in states]) > 0):
			#print("Reached %d states" % counter)
			if(num != initNum and num > initNum):
				noExtinct.append(num)
				numSaved[0] = numSaved[0] + 1
			return True
		states.append(num)
		
		if(isExtinct(state)):
			#print("Goes extinct after %d states" % counter)
			return False
		"""
		if(statesEqual(state,initState)):
			print("Checked for equal states")
			print("Reached %d states" % counter)
			return True
		"""
		counter = counter + 1
		if(counter > 2**(n*n)-1):
			break
	
	print("Reached maximum states")
	return -1 #Something wrong happened!
	
def num2state(num, n):
	"""
	Returns a state that is represented by num in n**2 bits
	A state is an nxn grids of 1s and 0s.
	"""
	numBits = n**2
	if(num > 2**numBits-1):
		print("%d cannot be represented by %d bits" % (num, numBits))
		return -1
	
	state = [[0]*n for x in range(n)]
	
	count = numBits-1
	i = 0
	j = 0
	index = n-1
	
	while(num > 0):
		state[i][j] = num%2
		num = int(math.floor(num/2))
		j = j + 1
		
		if(j > index):
			j = 0
			i = i + 1
			
		
		count = count - 1
		if(count < 0):
			break
	
	return state

def state2num(state):
	"""
	Returns a n**2-bit number that represents the state,
	where n is the size of the nxn state.
	"""
	
	n = len(state)
	weight = 0
	num = 0
	for i in range(n):
		for j in state[i]:
			num = num + (2**weight)*j
			weight = weight+1
	
	return num
