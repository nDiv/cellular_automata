#include <iostream>
#include <stdio>
#include <vector>

class gridState{
	  std::vector<bool> cells;
	  size_t size;
	  size_t length;
	
	public:
		gridState(size_t);
    size_t live_neighbors(size_t, size_t);
    void nextGen();
    size_t state2Int();
    void createFromInt(size_t);
    void printState();
};
