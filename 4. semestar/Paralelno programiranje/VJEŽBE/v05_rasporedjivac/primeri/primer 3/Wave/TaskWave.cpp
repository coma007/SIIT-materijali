//==============================================================
// Primer grafa zadataka za tzv. front-talasa, na bazi rekurzivne funkcije
// Predmet: Paralelno programiranje
// Pripremio: Odsek RT-RK
// =============================================================

#include <array>
#include <vector>
#include <iostream>

#include <tbb/blocked_range.h>
#include "tbb/task_group.h"
#include "tbb/tick_count.h"

using namespace std;
using namespace tbb;

const int n = 4;
const int A_size = n * n;
vector<double> A(A_size);                   // data
vector<atomic<int>> counters(A_size);       // atomic sync counters

// Simple wavefront function
double foo(double current, double above, double left) {
    for (int i = 0; i < 100000000; i++) {}  // work simulation
    return (current + above + left);        
}

// Serial wavefront
void wave(std::vector<double>& A, int n) {
    for (int i = 1; i < n; i++)
        for (int j = 1; j < n; j++) {
            A[i * n + j] = foo(A[i * n + j], A[(i - 1) * n + j], A[i * n + (j - 1)]);
            cout << "Executed task " << i * n + j << endl;
        }
}

// Parallel wavefront
void wave_p(std::vector<double>& A, int n, int i, int j) {
    task_group g;
    A[i * n + j] = foo(A[i * n + j], A[(i - 1) * n + j], A[i * n + (j - 1)]);
    cout << "Executed task " << i * n + j << endl;
    if (j < n - 1 && --counters[i * n + (j + 1)] == 0)      // right task ready
        g.run([&] {wave_p(A, n, i, j + 1); });              // spawn right task
    if (i < n - 1 && --counters[(i + 1) * n + j] == 0)      // lower task ready
        g.run([&] {wave_p(A, n, i + 1, j); });              // spawn lower task
    g.wait();                                               // wait for right and lower tasks
}

// Initialize atomic sync counters
void initcounters(std::vector<std::atomic<int>>& counters, int n) {
    for (auto& s : counters) s = 0;
    for (int i = 1; i < n; i++)
        counters[i * n + 1] = 1;            // (for i = 1 to n-1) && (j = 1): counters[i][j] = 1
    for (int j = 1; j < n; j++)
        counters[1 * n + j] = 1;            // (i = 1) && (for j = 1 to n-1): counters[i][j] = 1
    counters[1 * n + 1] = 0;                // i=1 and j=1: counters[i][j] = 0    ??
    for (int i = 2; i < n; i++)
        for (int j = 2; j < n; j++)
            counters[i * n + j] = 2;        // all inner counters set to 2
}


void printvec(const char* text, const std::vector<double>& vec) {
    cout << text;
    int sqr_size = 0;
    //for (const auto& s : vec) std::cout << s << ' ';
    for (auto it = vec.begin(); it != vec.end(); it++) {
        cout << *it << ' ';
        sqr_size++;
        if (sqr_size % n == 0) {
            cout << "\n";
        }
    }
    cout << "\n";
}

void printcnts(const char* text, const std::vector<std::atomic<int>>& cnt) {
    cout << text;
    int cnts = 0;
    //for (const auto& s : cnt) std::cout << s << ' ';
    for (auto it = cnt.begin(); it != cnt.end(); it++) {
        cout << *it << ' ';
        cnts++;
        if (cnts % n == 0) {
            cout << "\n";
        }
    }
    cout << "\n";
}

int main() {
    initcounters(counters, n);
    printcnts("Initial counters = \n", counters);

    for (auto& s : A) s = 1.0;
    printvec("Input A = \n", A);
    tick_count startTime = tick_count::now();
    wave(A, n);
    tick_count endTime = tick_count::now();
    printvec("wave out A = \n", A);
    cout << endl << "Serial time: " << (endTime - startTime).seconds() * 1000 << "ms." << endl << endl;

    for (auto& s : A) s = 1.0;
    printvec("Input A = \n", A);
    startTime = tick_count::now();
    wave_p(A, n, 1, 1);        // Launch wave_p with i=1 and j=1
    endTime = tick_count::now();
    printvec("wave_p out A = \n", A);
    cout << endl << "Parallel time: " << (endTime - startTime).seconds() * 1000 << "ms." << endl << endl;
    printcnts("Final counters = \n", counters);
}

