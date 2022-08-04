#include "utils.h"

void init_matrix(int *matrix, int m, int n){
	int data_size = m*n;
	for(int i = 0; i < data_size; ++i){
		matrix[i] = i;
	}
}

void print_matrix(int *matrix, int m, int n, char *name){
	cout << "[" << name << "]" << endl; 
	for(int i=0; i < m; i++){
		for(int j=0; j < n; j++){
			cout << matrix[i*n + j] << "\t"; 
		}
		cout << endl; 
	}
}

void matrix_addition_serial(int *io_matrix, int *i_matrix, int m, int n){
	for(int i=0; i < m; i++){
		for(int j=0; j < n; j++){
			io_matrix[i*n + j] += i_matrix[i*n + j];
		}
	}
}

bool check_results(int *matrix1, int *matrix2, int m, int n){
	for(int i=0; i < m; i++){
		for(int j=0; j < n; j++){
			if(matrix1[i*n + j] != matrix2[i*n + j]){
				return false;
			}
		}
	}
	return true;
}