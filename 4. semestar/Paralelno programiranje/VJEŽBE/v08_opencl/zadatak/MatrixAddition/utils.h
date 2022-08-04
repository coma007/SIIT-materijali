#ifndef UTILS_H
#define UTILS_H

#include <stdlib.h>
#include <stdio.h>
#include <iostream>

using namespace std;

void init_matrix(int *matrix, int m, int n);

void print_matrix(int *matrix, int m, int n, char *name);

void matrix_addition_serial(int *io_matrix, int *i_matrix, int m, int n);

bool check_results(int *matrix1, int *matrix2, int m, int n);


#endif /* UTILS_H */