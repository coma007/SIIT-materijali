#include <stdio.h>
#include <float.h>
#include <iostream>

#include "tbb\tbb.h"
#include "tbb\parallel_reduce.h"

using namespace tbb;

float Foo(float a) {
	return a;
}

   //TODO: Create a class called MinIndexFoo with constructors, operator() and the join method

class MinIndexFoo {
public:
	const float* my_a;
	float value_of_min;
	float index_of_min;

	MinIndexFoo(const float* a) : my_a(a), value_of_min(FLT_MAX), index_of_min(-1) {};
	MinIndexFoo(MinIndexFoo& x, split) : my_a(x.my_a), value_of_min(x.value_of_min), index_of_min(x.index_of_min) {};

	void join(const MinIndexFoo& x) {
		if (x.value_of_min < value_of_min) {
			index_of_min = x.index_of_min;
		}
	}

	void operator() (const blocked_range<size_t>& r) {
		const float* a = my_a;
		for (size_t i = r.begin(); i != r.end(); ++i) {
			float value = Foo(a[i]);
			if (value < value_of_min) {
				value_of_min = value;
				index_of_min = i;
			}
		}
	}
};

   //TODO: Create a function for parallel minimum

long ParallelMinIndexFoo(const float a[], size_t n) {
	MinIndexFoo mif(a);
	parallel_reduce(blocked_range<size_t>(0, 100, 5), mif);
	return mif.index_of_min;
}

int main () {
	float a[100];

	for (int i=0; i<100; ++i) {
		a[i] = -i;
	}

	tbb::tick_count startTime = tbb::tick_count::now();
	long ind = ParallelMinIndexFoo(a, 100);
	printf("Result: %d\n", ind);
	tbb::tick_count endTime = tbb::tick_count::now();
	std::cout << "Parallel time: " << (endTime - startTime).seconds() << std::endl;

	
	return 0;
}