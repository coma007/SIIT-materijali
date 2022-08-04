#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"
#include "tbb/tick_count.h"
#include <iostream>

using namespace tbb;
using namespace std;

//TODO: Create a class/structure for paralelization
class Average {
public:
	double* input;
	double* output;
	void operator() (const blocked_range<size_t>& range) const {
		for (int i=range.begin(); i != range.end(); ++i) {
			output[i] = (input[i] + input[i + 1] + input[i + 2]) * (1 / 3.0f);
		}
	}
};
// Note: The input must be padded such that input[-1] and 
// input[n] can be used to calculate the first and last 
// output values.

//TODO: Create a funcion for paralelization

// Sets output[i] to the average of input[i-1], input[i] and input[i+1]
int main() {
	double input[1002], output_serial[1000], output_parallel[1000];
	int test = 0;

	input[0] = 0;
	input[1001] = 0;
	for (int i = 1; i < 1001; i++) {
		input[i] = i * 3.14;
	}

	tick_count startTime = tick_count::now();
	for (int i = 0; i < 1000; i++) {
		output_serial[i] = (input[i] + input[i + 1] + input[i + 2])*(1 / 3.0f);
	}
	tick_count endTime = tick_count::now();

	cout << "Serial time: " << (endTime - startTime).seconds() << endl;

	//TODO: Paralell average
	Average a;
	a.input = input;
	a.output = output_parallel;
	startTime = tick_count::now();
	parallel_for(blocked_range<size_t>(0, 1000, 500), a);
	endTime = tick_count::now();
	cout << "Parallel time: " << (endTime - startTime).seconds() << endl;

	//TODO: Check if the results are equal
	int fails = 0;
	for (int i = 0; i < 1000; i++) {
		if (output_serial[i] != output_parallel[i]) {
			fails++;
		}
	}
	
	cout << "Fails: " << fails;

	return 0;
}
