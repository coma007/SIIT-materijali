#include "Matrix.h"

Matrix::Matrix() : dim1(0), dim2(0) {
	elems.resize(dim1 * dim2);
	for (int i = 0; i < dim1; i++) {
		for (int j = 0; j < dim2; j++) {
			Matrix::UpdateElement(i, j, 0);
		}
	}
}

Matrix::Matrix(int dim1, int dim2) : dim1(dim1), dim2(dim2) {
	elems.resize(dim1*dim2);
	for (int i = 0; i < dim1; i++) {
		for (int j = 0; j < dim2; j++) {
			Matrix::UpdateElement(i, j, 0);
		}
	}
}

Matrix::Matrix(int dim1, int dim2, int value) : dim1(dim1), dim2(dim2) {
	elems.resize(dim1*dim2);
	for (int i = 0; i < dim1; i++) {
		for (int j = 0; j < dim2; j++) {
			Matrix::UpdateElement(i, j, value);
		}
	}
}

bool Matrix::UpdateElement(int i1, int i2, int value) {
	this->elems[i2+ i1*dim1] = value;
	return true;
}

bool Matrix::PrintElement(int i1, int i2) {
	cout << "[" << i1 << "][" << i2 << "] = " << elems[i2+i1*dim1] << endl;
	return true;
}

void Matrix::Print() {
	cout << "[";
	for (int i = 0; i < dim1; i++) {
		cout << endl;
		for (int j = 0; j < dim2; j++) {
			cout << elems[j+i*dim1] << " ";
		}
	}
	cout << endl << "]" << endl;
}