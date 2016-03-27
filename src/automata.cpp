#include "../include/automata.h"

//using namespace std;

gridState::gridState(size_t size){
	this.size = size;
	this.length = size*size;
}

void createFromInt(size_t num){
	std::vector<bool> state:
