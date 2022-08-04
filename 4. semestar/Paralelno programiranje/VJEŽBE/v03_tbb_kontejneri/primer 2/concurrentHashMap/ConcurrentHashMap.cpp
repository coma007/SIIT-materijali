#include "tbb/concurrent_hash_map.h"
#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"
#include <iostream>

using namespace std;
using namespace tbb;

// TODO: Create a simple MyHashCompare structure
struct MyHashCompare {
	static int hash(const int& x) {
		return x;
	}

	static bool equal(const int& x, const int& y) {
		return x == y;
	}
};

// A concurrent hash table that maps ints to ints
typedef concurrent_hash_map<int, int, MyHashCompare> IntTable;

// TODO: Create a simple Histogram class which will count the number of occurrences
struct Histogram {
	IntTable& table;

	Histogram(IntTable& table_) : table(table_) {}

	void operator() (const blocked_range<int*> range) const {
		for (int* p = range.begin(); p != range.end(); p++) {
			IntTable::accessor a;
			table.insert(a, *p);
			a->second += 1;
		}
	}
};

const size_t N = 1000000;
int Data[N];

// Count occurrences
void main() {
	// Construct empty table
	IntTable table;
	IntTable table_parallel;
	IntTable::iterator i;
	
	// Create some data to work with
	for (int i = 0; i < N; i++) {
		Data[i] = rand() % 10;
	}



	// TODO: Put occurrences into the table using parallel_for
	Histogram h_parallel(table_parallel);
	parallel_for(blocked_range<int*>(&Data[0], &Data[0]+N), h_parallel);
	// Display the occurrences
	for (i = table_parallel.begin(); i != table_parallel.end(); i++) {
		cout << i->second << endl;
	}
}
