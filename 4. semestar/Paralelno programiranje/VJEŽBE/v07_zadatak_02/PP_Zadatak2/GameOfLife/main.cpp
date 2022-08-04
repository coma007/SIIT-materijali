#include "GameOfLife.h"
#include <iostream>
#include <string>
#include "string.h"
#include <tbb/tick_count.h>

#define NUM_OF_ITERATIONS 27
#define TABLE_SIZE 256

// PARALLEL IS SLIGHTLY FASTER
//#define NUM_OF_ITERATIONS 27
//#define TABLE_SIZE 128

using namespace std;
using namespace tbb;

static void printTable(GameOfLife *game, int iterNum);

int main(int argc, char *argv[]) {

	unsigned long long startTicks, endTicks;

	GameOfLife game(TABLE_SIZE, TABLE_SIZE, PULSAR);
	int rebornCells = 0;

	// serial version
	cout << "Serial Game of Life initiated..." << endl;
	tick_count startTime = tick_count::now();
	for (int i = 0; i < NUM_OF_ITERATIONS; i++) {
		//printTable(&game, i);
		rebornCells += game.nextIterSerial();
	}
	tick_count endTime = tick_count::now();
	cout << "Serial time: \t\t\t" << (endTime - startTime).seconds() << " seconds\n";
	cout << "Reborn cells: \t\t\t" << rebornCells << endl;
	
	// parallel version


	rebornCells = 0;
	cout << "Parallel Game of Life initiated..." << endl;
	startTime = tick_count::now();
	for (int i = 0; i < NUM_OF_ITERATIONS; i++) {
		//printTable(&game, i);
		rebornCells += game.nextIterParallel(0, 0, TABLE_SIZE);
	}
	endTime = tick_count::now();
	cout << "Parallel time: \t\t\t" << (endTime - startTime).seconds() << " seconds\n";
	cout << "Reborn cells: \t\t\t" << rebornCells << endl;

	return 0;
}

static void printTable(GameOfLife *game, int iterNum){	

	cout << "Iteration: " << iterNum << endl;
	game->printIteration();
	system("pause");
	system("cls");

	return;
}