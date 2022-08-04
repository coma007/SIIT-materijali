#include <iostream>
#include <vector>
#include <math.h>

#include "tbb/task_group.h"
#include <tbb/tick_count.h>


using namespace std;
using namespace tbb;

#define delta 0.000001
#define LOWER 0
#define UPPER 3.14

#define CutOff 0.01

//wolfram alfa formula: (integrate exp(-1/x) cos(x) from x = 0 to 3.14)
//result -0.495667

double calculation(double x);
double incremental(double lowerBound, double upperBound);
double serial_integration(double lowerBound, double upperBound);
double parallel_integration(double lowerBound, double upperBound);

int main() {
	double serialResult = 0;
	double parallelResult = 0;

	cout << "Serial integral function..." << endl;
	tick_count startTime = tick_count::now();
	serialResult = serial_integration(LOWER, UPPER);
	tick_count endTime = tick_count::now();
	cout << "Serial result: " << serialResult << endl;
	cout << "Calcualtions took " << (endTime - startTime).seconds() << " seconds." << endl << endl;

	cout << "Paralel integral function..." << endl;
	startTime = tick_count::now();
	parallelResult = parallel_integration(LOWER, UPPER);
	endTime = tick_count::now();
	cout << "Paralel result: " << parallelResult << endl;
	cout << "Calcualtions took " << (endTime - startTime).seconds() << " seconds." << endl;

	return 0;
}

double calculation(double x) {
    return exp(-1 / x) * delta * cos(x);
}

double incremental(double lowerBound, double upperBound) {
	double res = 0;
	for (double iter = lowerBound; iter <= upperBound; iter += delta)
	{
		res += calculation(iter);
	}
	return res;
}

double serial_integration(double lowerBound, double upperBound) {

	double value = 0;
	for (double i = lowerBound; i <= upperBound; i += delta) {
		value += exp(-1 / i) * cos(i) * delta;
	}
	return value;
}

double parallel_integration(double lowerBound, double upperBound) {
	
	double value = 0;
	task_group g;

	if (upperBound - lowerBound < CutOff) {
		value += serial_integration(lowerBound, upperBound);
	}
	else {
		double x, y;
		g.run([&] {x = parallel_integration(lowerBound, lowerBound + (upperBound - lowerBound) / 2);});
		g.run([&] {y = parallel_integration(lowerBound + (upperBound - lowerBound) / 2, upperBound);});
		g.wait();
		value += x + y;
	}

	return value;
}

// next : Game of Life