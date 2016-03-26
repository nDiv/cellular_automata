#test.py
"""
Script for testing the automata code
"""

from automata import Cell
from automata import GridState as State
import time

"""
state = State(4)
state.stateFromInt(1)
print(state.state2Int())
state.printState()
state.nextGen()
state.printState()
"""


# Main program starts here.
startT = time.time()
	
n = 4
lives = 0
#NoExtinct = []
#Extinct = []
for i in range(1,2**(n*n)): # Loop through all possible states except the zero state.
	"""
	if(i in NoExtinct):
		lives += 1
		continue

	if(i in Extinct):
		continue
	"""

	state = State(n)
	state.stateFromInt(i)
	states = [i]
	while(True):
		state.nextGen()
		stateNum = state.state2Int()

		if(stateNum == 0):
			#Extinct = Extinct + states
			#Extinct = list(set(Extinct))
			break
		elif(stateNum in states):
			lives += 1
			#NoExtinct = NoExtinct + states
			#NoExtinct = list(set(NoExtinct))
			break
		else:
			states.append(stateNum)
		
	if(i%10000 == 0):
		currentT = time.time()
		print("Loop: %d, time: %f seconds" % (i,currentT-startT))
		
endT = time.time()
print("It took %f seconds" % (endT-startT))
print("Immortal states: %d" % lives)

