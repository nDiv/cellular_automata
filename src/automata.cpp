#include "automata.h"

gridState::gridState(int size){
	this->size = size;
	this->length = size*size;
}

void gridState::createFromInt(int num){
	std::vector<int> state;
	
	while(num > 0){
		state.insert(state.begin(), (int) num%2);
		num = (int) floor(num/2);
	}

	if((int) state.size() != this->length){
		int i = this->length - (int) state.size();
		while(i > 0){
			state.insert(state.begin(), 0);
			i--;
		}
	}
	this->cells = state;
}

int gridState::getSize(void){
	return this->size;
}

int gridState::getLen(void){
	return this->length;
}

void gridState::printState(void){
	if(sizeof(this->cells) != 0){
		std::cout<<"State: "<<std::endl;
		for(int j=0; j < this->size; j++){
			for(int i=0; i < this->size; i++){
				std::cout<<this->cells[i+(j*this->size)]<<" ";
			}
			std::cout<<std::endl;
		}
	}else{
		std::cout<<"State is empty!"<<std::endl;
	}
}

int gridState::state2Int(void){
	int num = 0;
	int weight = this->length - 1;
	for(int i=0; i < this->length; i++){
		num = num + (pow(2,weight)*cells[i]);
		weight--;
	}
	return num;
}

int gridState::live_neighbors(int i, int j){
	int live = 0;
	int const n = 8;
	std::array<int, n> x; 
	std::array<int, n> y;
	x[0] = i-1;
	x[1] = i-1;
	x[2] = i-1;	
	x[3] = i;
	x[4] = i;
	x[5] = i+1;
	x[6] = i+1;
	x[7] = i+1;
	
	y[0] = j-1;
	y[1] = j;
	y[2] = j+1;
	y[3] = j-1;
	y[4] = j+1;
	y[5] = j-1;
	y[6] = j;
	y[7] = j+1;
	
	for(int t = 0; t < n; t++){
		if(x[t]>=0 && x[t] < this->size && y[t]>=0 && y[t] < this->size){
			if(this->cells[y[t]+(x[t]*this->size)] == 1){
				live++;
			}
		}
	}
	return live;
}

void gridState::nextGen(void){
	std::vector<int> nState;
	
	for(int i=0; i<this->size; i++){
		for(int j=0; j<this->size; j++){
			int nb_sum = this->live_neighbors(i,j);
			if(nb_sum == 1 || nb_sum == 2){
				nState.push_back(1);
			}else{
				nState.push_back(0);
			}
		}
	}
	this->cells = nState;
}
