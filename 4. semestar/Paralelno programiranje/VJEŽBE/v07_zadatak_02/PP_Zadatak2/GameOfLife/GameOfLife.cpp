#include "GameOfLife.h"
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
using namespace tbb;

GameOfLife::GameOfLife(unsigned int height_, unsigned int width_, InitModel model) {

	height = height_;
	width = width_;

	buffer = new unsigned char[width * height];
	nextIter = new unsigned char[width * height];

	grain_size = width / 16;

	// fill buffer
	switch(model){        
	case PULSAR:
		{
			if(width > 15 && height > 15){
				memset(buffer, 0x0, width * height * sizeof(unsigned char));
				buffer[2 * width + 4] = 1;
				buffer[2 * width + 5] = 1;
				buffer[2 * width + 6] = 1;

				buffer[2 * width + 10] = 1;
				buffer[2 * width + 11] = 1;
				buffer[2 * width + 12] = 1;

				buffer[4 * width + 2] = 1;
				buffer[5 * width + 2] = 1;
				buffer[6 * width + 2] = 1;

				buffer[4 * width + 7] = 1;
				buffer[5 * width + 7] = 1;
				buffer[6 * width + 7] = 1;

				buffer[4 * width + 9] = 1;
				buffer[5 * width + 9] = 1;
				buffer[6 * width + 9] = 1;

				buffer[4 * width + 14] = 1;
				buffer[5 * width + 14] = 1;
				buffer[6 * width + 14] = 1;

				buffer[7 * width + 4] = 1;
				buffer[7 * width + 5] = 1;
				buffer[7 * width + 6] = 1;

				buffer[7 * width + 10] = 1;
				buffer[7 * width + 11] = 1;
				buffer[7 * width + 12] = 1;

				buffer[9 * width + 4] = 1;
				buffer[9 * width + 5] = 1;
				buffer[9 * width + 6] = 1;

				buffer[9 * width + 10] = 1;
				buffer[9 * width + 11] = 1;
				buffer[9 * width + 12] = 1;

				buffer[10* width + 2] = 1;
				buffer[11* width + 2] = 1;
				buffer[12* width + 2] = 1;

				buffer[10* width + 7] = 1;
				buffer[11* width + 7] = 1;
				buffer[12* width + 7] = 1;

				buffer[10* width + 9] = 1;
				buffer[11* width + 9] = 1;
				buffer[12* width + 9] = 1;

				buffer[10* width + 14] = 1;
				buffer[11* width + 14] = 1;
				buffer[12* width + 14] = 1;

				buffer[14* width + 4] = 1;
				buffer[14* width + 5] = 1;
				buffer[14* width + 6] = 1;

				buffer[14* width + 10] = 1;
				buffer[14* width + 11] = 1;
				buffer[14 * width + 12] = 1;

				break;
			}
		}

	case RABBITS:
		{
			if(width > 15 && height > 15){
				memset(buffer, 0x0, width * height * sizeof(unsigned char));
				buffer[2 * width + 4] = 1;
				buffer[2 * width + 5] = 1;
				buffer[2 * width + 6] = 1;

				buffer[3 * width + 6] = 1;
				buffer[3 * width + 7] = 1;
				buffer[3 * width + 9] = 1;

				buffer[4 * width + 3] = 1;
				buffer[4 * width + 5] = 1;
				buffer[4 * width + 6] = 1;
				buffer[4 * width + 7] = 1;
				buffer[4 * width + 8] = 1;
				buffer[4 * width + 9] = 1;

				break;
			}
		}

	case PHI:
		{
			if(width > 15 && height > 15){
				memset(buffer, 0x0, width * height * sizeof(unsigned char));
				buffer[3 * width +  4] = 1;
				buffer[3 * width +  8] = 1;

				buffer[4 * width +  5] = 1;
				buffer[4 * width +  6] = 1;
				buffer[4 * width +  7] = 1;

				buffer[5 * width +  5] = 1;
				buffer[5 * width +  6] = 1;
				buffer[5 * width +  7] = 1;

				buffer[6 * width +  4] = 1;
				buffer[6 * width +  8] = 1;

				break;
			}
		}

	case RANDOM:
	default: 
		{
			if (model != RANDOM){
				cout << "Using RANDOM as default setup" << endl;
			}
			srand ( time(NULL) );
			for(unsigned int i = 0; i < height; i++){
				for(unsigned int j = 0; j < width; j++){
					buffer[i * width + j] = rand() % 2;
				}
			}
		}
	}
}

void GameOfLife::printIteration() {

	for (int row = 0; row < height; row++) {
		for (int col = 0; col < width; col++) {            

			char c;

			if(buffer[row * width + col] == 1) c = 0xb2;
			else c = 0x20;

			cout << c << " ";
		}
		cout << "\n";
	}
}

int GameOfLife::getNeighbourSum(unsigned int row, unsigned int col) {

	int sum = 0;
	int lowerI, upperI;
	int lowerJ, upperJ;

	// matrix limits
	lowerI = (col > 0) ? -1 : 0;
	upperI = (col < width -1) ? 1 : 0;
	lowerJ = (row > 0) ? -1 : 0;
	upperJ = (row < height -1) ? 1 : 0;

	for (int m = col + lowerI; m <= col + upperI; m++) {
		for (int n = row + lowerJ; n <= row + upperJ; n++) {
			if ((m != col) || (n != row)) {
				sum += buffer[n * width + m];
			}
		}
	}

	return sum;
}

int GameOfLife::nextIterSerial() {

	int rebornCells = 0;
	for (int row = 0; row < height; row++) {
		for (int col = 0; col < width; col++) {
			int neighbours = getNeighbourSum(row, col);
			if (buffer[row * width + col] == 1) {
				if ((neighbours == 2) || (neighbours == 3)) {
					nextIter[row * width + col] = 1;
				} else {
					nextIter[row * width + col] = 0;
				}
			} else {
				if (neighbours == 3) {
					nextIter[row * width + col] = 1;
					rebornCells++;
				} else {
					nextIter[row * width + col] = 0;
				}
			}
		}
	}

	// swtich buffers
	unsigned char * temp = buffer;
	buffer = nextIter;
	nextIter = temp;

	return rebornCells;
}

int GameOfLife::nextIterParallel(int _row, int _col, int _width) {

	int rebornCells = 0;
	// TODO: PLACE CODE HERE
	if (_width < grain_size) {
		for (int row = _row; row < _row + _width; row++) {
			for (int col = _col; col < _col + _width; col++) {
				int neighbours = getNeighbourSum(row, col);
				if (buffer[row * width + col] == 1) {
					if ((neighbours == 2) || (neighbours == 3)) {
						nextIter[row * width + col] = 1;
					}
					else {
						nextIter[row * width + col] = 0;
					}
				}
				else {
					if (neighbours == 3) {
						nextIter[row * width + col] = 1;
						rebornCells++;
					}
					else {
						nextIter[row * width + col] = 0;
					}
				}
			}
		}
	}
	else {
		task_group t;
		int a = 0, b = 0, c = 0, d = 0;
		t.run([&] {a = nextIterParallel(_row, _col, _width / 2); });
		t.run([&] {b = nextIterParallel(_row + _width / 2, _col, _width / 2); });
		t.run([&] {c = nextIterParallel(_row, _col + _width / 2, _width / 2); });
		t.run([&] {d = nextIterParallel(_row + _width / 2, _col + _width / 2, _width / 2); });
		t.wait();
		rebornCells = a + b + c + d;
	}

	// swtich buffers
	if (_width == width) {
		unsigned char* temp = buffer;
		buffer = nextIter;
		nextIter = temp;
	}

	return rebornCells;
}

GameOfLife::~GameOfLife() {

	if(buffer){
		delete buffer;
	}
	if(nextIter){
		delete nextIter;
	}
}

