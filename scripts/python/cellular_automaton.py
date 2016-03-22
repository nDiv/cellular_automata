import math
import time

def isExtinct(state):
	extinct = True
	
	for i in range(len(state)):
		for j in state[i]:
			if(j == 1):
				extinct = False
				break
	return extinct
	
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
