#automata.py
"""
A script containing Grid and Cell clases for the automata challenge
"""

class Cell:
	
	def __init__(self, x, y, state):
		self.x = x
		self.y = y
		self.state = state

class GridState:

	def __init__(self, size):
		#self.cells = [Cell(0,0,False) for x in range(size*size)]
		self.cells = []
		self.size = size
		self.length = size*size

	def getCellState(self, x, y):
		return self.cells[x + y*self.size].state

	def setCellState(self, x, y, state):
		self.cells[x + y*self.size].state = state

	def nextGen(self):
		nCells = []
		for cell in self.cells:
			live = self.live_neighbors(cell.x,cell.y)
			if(live == 1 or live == 2):
				nCells.append(Cell(cell.x, cell.y, True))
			else:
				nCells.append(Cell(cell.x, cell.y, False))
		self.cells = nCells

	def live_neighbors(self, i, j):
		live = 0
		nx = [i-1,i-1,i-1,i,i,i+1,i+1,i+1]
		ny = [j-1,j,j+1,j-1,j+1,j-1,j,j+1]	
		for x, y in zip(nx,ny):
			if(x>=0 and x<self.size and y>=0 and y<self.size):
				if(self.cells[y + x*self.size].state):
					live += 1
		return live
	
	def state2Int(self):
		strState = ''
		for cell in self.cells:
			strState = strState + str(int(cell.state))

		return int(strState,2)

	def stateFromInt(self, num):
		strnum = "{0:b}".format(num).zfill(self.length)

		index = 0
		i = 0
		j = 0
		while(index < self.length):
			self.cells.append(Cell(i,j,bool(int(strnum[index]))))
			"""
			self.cells[index].state = bool(int(strnum[index]))
			self.cells[index].x = i
			self.cells[index].y = j
			"""
			
			j = j + 1
		
			if(j > self.size-1):
				j = 0
				i += 1
			index += 1

	def isExtinct(self):
		return self.state2Int() == 0

	def printState(self):
		print("----")
		for i in range(self.size):
			for j in range(self.size):
				print(int(self.cells[j+i*self.size].state), end='')
			print("\n")
		print("----")

