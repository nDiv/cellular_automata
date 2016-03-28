#include "automata.h"
#include <time.h>
#include <algorithm>

using namespace std;

int main(void)
{
	int const n = 4; //Grid size.
	int lives = 0; //Counter for surviving states.

	const clock_t begin_time = clock();
	
	for(int i=1; i<pow(2,n*n); i++){
		gridState state = gridState(n);
		state.createFromInt(i);
		vector<int> states;
		states.push_back(i);
		
		while(true){
			state.nextGen();
			int stateNum = state.state2Int();
			
			if(stateNum == 0){
				break;
			}else if(find(states.begin(), states.end(), stateNum) != states.end()){
				lives++;
				break;
			}else{
				states.push_back(stateNum);
			}
		}
		if(i%10000 == 0){
			cout<<"Loop: "<<i<<", time: "<<float( clock () - begin_time ) /  CLOCKS_PER_SEC<<" seconds."<<endl;
		}
	}
	float end_time = float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	cout<<"It took "<<end_time<<" seconds..."<<endl;
	cout<<"Survived states: "<<lives<<endl;
	return 0;
}
