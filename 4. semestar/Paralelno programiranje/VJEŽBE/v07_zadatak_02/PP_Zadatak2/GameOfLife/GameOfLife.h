#pragma once

#include "tbb/task_group.h"

typedef enum InitModel{
	RANDOM, 
	PULSAR, 
	RABBITS, 
	PHI
};

class GameOfLife {
private:	

	//! board width and height
	unsigned int width, height;

	//! holds init board state
	unsigned char *buffer;

	//! holds next iteration board state
	unsigned char *nextIter;

	//! grain size 
	unsigned char grain_size;

	/**
	* @brief Calculate how much neighbours cell has.
	* 
	* @param row cell row
	* @param col cell column
	*/
	int getNeighbourSum(unsigned int row, unsigned int col);

	/**
	* @brief Do game of life algorithm for cells is one board row.
	* 
	* @param nextIter pointer to buffer for next iteration
	* @param row board row
	*/
	void processRow(unsigned char *nextIter, unsigned int row);

public:

	// ! reborn cells
	/*unsigned int rebornCells;*/

	/**
	* @brief Constuctor.
	*
	* @param height_ board height
	* @param width_ board withd
	* @param model init board model
	*/
	GameOfLife(unsigned int height_, unsigned int width_, InitModel model);

	/**
	* @brief default destructor.
	*/
	~GameOfLife();

	/**
	* @brief Game of life serial version for one iteration.
	*/
	int nextIterSerial();

	/**
	* @brief Game of life parallel version for one iteration.
	*/
	int nextIterParallel(int _i, int _j, int _w);

	/**
	* @brief Print board to console.
	*/
	void printIteration();

	/**
	* @brief Implements divide & conquer.
	*/
	void applyDAC(int _row, int _col, int _width);

	/**
	* @brief Calculate cells next state.
	*/
	void getNextIter(int _row, int _col, int _width);
};
