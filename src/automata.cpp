#include "../include/automata.h"

//using namespace std;

gridState::gridState(int size){
	this->size = size;
	this->length = size*size;
}

void gridState::createFromInt(int num){
	std::vector<int> state;
	
	while(num > 0){
		state.insert(state.begin(), num%2);
		num = (int) floor(num/2);
	}

	if(sizeof(state) != this->length){
		int i = this->length - sizeof(state);
		while(i > 0){
			state.insert(state.begin(), 0);
			i--;
		}
	}
	this->cells = state;
}
