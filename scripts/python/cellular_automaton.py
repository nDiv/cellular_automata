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
