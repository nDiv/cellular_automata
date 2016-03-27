#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>

class gridState{
	  std::vector<int> cells;
	  int size;
	  int length;
	
	public:
		gridState(int);
    //int live_neighbors(int, int);
    //void nextGen();
    //int state2Int();
    void createFromInt(int);
    //void printState();
};
