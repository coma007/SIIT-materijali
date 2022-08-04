#include <stdio.h>
#include <float.h>
#include "tbb/tick_count.h"
#include <iostream>

float Foo(float a) {
	return a;
}

long SerialMinIndexFoo (const float a[], size_t n) {
	float value_of_min = FLT_MAX;   // FLT_MAX from <float.h>
	long index_of_min = -1;
	for( size_t i=0; i<n; ++i ){
		float value = Foo(a[i]);
		if (value < value_of_min) {
			value_of_min = value;
			index_of_min = i;
		}
	}
	return index_of_min;
}

int main () {


	float a[100];

	for (int i=0; i<100; ++i) {
		a[i] = (float)-i;
	}
	
	tbb::tick_count startTime = tbb::tick_count::now();
	long ind = SerialMinIndexFoo(a, 100);
	printf("Result: %d\n", ind);
	tbb::tick_count endTime = tbb::tick_count::now();
	std::cout << "Serial time: "  << (endTime - startTime).seconds() << std::endl;

	return 0;
}