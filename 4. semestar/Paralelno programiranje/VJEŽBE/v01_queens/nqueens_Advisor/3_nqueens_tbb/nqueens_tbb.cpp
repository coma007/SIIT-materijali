//=======================================================================
//
// SAMPLE SOURCE CODE - SUBJECT TO THE TERMS OF END-USER LICENSE AGREEMENT FOR
// INTEL(R) PARALLEL ADVISOR 2011.
//
// Copyright 2009-2010 Intel Corporation
//
// THIS FILE IS PROVIDED "AS IS" WITH NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT
// NOT LIMITED TO ANY IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
// PURPOSE, NON-INFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS.
//
// ========================================================================

// [DESCRIPTION]
// Solve the nqueens problem  - how many positions of queens can fit on a chess board
// of a given size without attacking each other.
// This is the serial version used to find a candidate hotspot function to parallelize.
//
// [BUILD]
// Use a Release configuration to ensure you find a hotspot representative of a final production build.
//
// [RUN]
// To set the board size in Visual Studio, right click on the project,
// select Properies > Configuration Properties > General > Debugging.  Set
// Command Arguments to the desired value.  13 has been set as the default.
//
// [EXPECTED OUTPUT]
//
// Board Size   Number of Solutions
//     4                2
//     5               10
//     6                4
//     7               40
//     8               92
//     9              352
//    10              724
//    11             2680
//    12            14200
//    13            73712
//    14           365596
//    15          2279184

#include <iostream>
#include <windows.h>
#include <mmsystem.h>
#include "tbb/task_scheduler_init.h"
#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"
#include "tbb/spin_mutex.h"

using namespace tbb;
using namespace std;

int nrOfSolutions=0;  //keeps track of the number of solutions
int boardSize=0;  // the board-size read from command-line
int correctSolution[16]; //array of the number of correct solutions for each board size

// define tbb mutexes
spin_mutex NrOfSolutionsMutex;

/*
Recursive function to find all solutions on a board 
represented by the argument "queens", placing the next queen
at location (row, col)

On Return: nrOfSolutions has been increased to add solutions for this board

*/
void setQueen(int queens[], int row, int col) {
    //check all previously placed rows for attacks
    for(int i=0; i<row; i++) {
        // vertical attacks
        if (queens[i]==col) {
            return;
        }
        // diagonal attacks
        if (abs(queens[i]-col) == (row-i)) {
            return;
        }
    }
    // column is ok, set the queen
    queens[row]=col;

    if(row==boardSize-1) {
        {      
            // increment is not atomic, so setting a lock is required here
            spin_mutex::scoped_lock mylock(NrOfSolutionsMutex);
            nrOfSolutions++;  //Placed final queen, found a solution!
        } // closing block invokes scoped_lock destructor which releases the lock

    }
    else {
        // try to fill next row
        for(int i=0; i<boardSize; i++) {
            setQueen(queens, row+1, i);
        }
    }
}

class SetQueens {
public:
    void operator()( const blocked_range<size_t>& r ) const {
        for( size_t i=r.begin(); i!=r.end(); ++i ) {
            // try all positions in first row
            // create separate array for each recursion
            // started here
            int* queens = new int[boardSize];
            setQueen(queens, 0, (int)i);
        }
    }
};

/*
Function to find all solutions for nQueens problem on size x size chessboard.

On Return: nrOfSoultions = number of solutions for size x size chessboard.
*/

void solve() {
    // Do a parallel for over the n positions in the first row.
    // Let the scheduler decide how the n tasks are distrubuted 
    // on the different threads
    parallel_for(blocked_range<size_t>(0, boardSize, 1), SetQueens());
}


int main(int argc, char* argv[]) {
    if(argc !=2) {
        cerr << "Usage: nqueens_tbb boardSize [default is 13].\n";
        boardSize = 13;
    } else {
        boardSize = atoi(argv[1]);
        if (boardSize < 4 || boardSize > 15) {
            cerr << "Boardsize should be between 4 and 15; setting it to 13. \n" << endl;
            boardSize = 13;
        }
    }
    // Set the expected number of solutions for each board-size for later checking.
    correctSolution[0] = 0;
    correctSolution[1] = 0;
    correctSolution[2] = 0;
    correctSolution[3] = 0;
    correctSolution[4] = 2;
    correctSolution[5] = 10;
    correctSolution[6] = 4;
    correctSolution[7] = 40;
    correctSolution[8] = 92;
    correctSolution[9] = 352;
    correctSolution[10] = 724;
    correctSolution[11] = 2680;
    correctSolution[12] = 14200;
    correctSolution[13] = 73712;
    correctSolution[14] = 365596;
    correctSolution[15] = 2279184;

    cout << "Starting 3_nqueens_tbb solver for size " << boardSize << "...\n";
    DWORD startTime=timeGetTime();
    // initialize tbb scheduler
    task_scheduler_init init;
    solve();
    DWORD endTime=timeGetTime();
    cout << "Number of solutions: " << nrOfSolutions << endl;
    if (nrOfSolutions != correctSolution[boardSize])
        cout << "!!Incorrect result!! Number of solutions should be " << correctSolution[boardSize] << endl << endl;
    else
        cout << "Correct result!" << endl;

    cout << endl << "Calculations took " << endTime-startTime << "ms.\n";

    return 0;
}
