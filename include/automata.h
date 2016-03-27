#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <array>

class gridState{
	  std::vector<int> cells;
	  int size;
	  int length;
	
	public:
		gridState(int);
    int live_neighbors(int, int);
    void nextGen();
    int state2Int(void);
    void createFromInt(int);
    void printState(void);
		int getSize(void);
		int getLen(void);
};
