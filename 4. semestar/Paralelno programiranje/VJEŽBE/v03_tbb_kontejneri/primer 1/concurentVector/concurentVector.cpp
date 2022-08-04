#include <vector>
#include "tbb/concurrent_vector.h"
#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"
#include "tbb/tick_count.h"
#include <iostream>

using namespace std;
using namespace tbb;

const size_t N = 100000000;
int Data[N];

vector<int> vect;
concurrent_vector<int> conVect;

void main() {

	cout << "Preparing data..." << endl;

	for (int i = 0; i < N; i++) {
		Data[i] = rand() % 10;
	}

	cout << "Data prepared. Adding elements to the vector." << endl;

	tick_count start = tick_count::now();
	for (int i = 0; i < N; i++) {
		vect.push_back(Data[i]);
	}
	tick_count end = tick_count::now();

	cout << "Adding elements to the vector lasted: " << (end - start).seconds() << " seconds." << endl;
	cout << "Adding elements to the concurrent vector." << endl;

	start = tick_count::now();
	for (int i = 0; i < N; i++) {
		conVect.push_back(Data[i]);
	}
	end = tick_count::now();

	cout << "Adding elements to the concurrent vector lasted: " << (end - start).seconds() << " seconds." << endl;
	getchar();
}