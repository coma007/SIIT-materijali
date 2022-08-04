#pragma once
#include <vector>
#include <iostream>

#include <iostream>
#include <vector>

using namespace std;

class MatrixInterface{
public:
	virtual bool UpdateElement(int, int, int) = 0;
	virtual bool PrintElement(int, int) = 0;
	virtual void Print() = 0;
};


class Matrix : public MatrixInterface  {
public:
	Matrix();
	Matrix(int dim1, int dim2);
	Matrix(int dim1, int dim2, int value);
	bool UpdateElement(int i1, int i2, int i3);
	bool PrintElement(int i1, int i2);
	void Print();
private:
	int dim1;
	int dim2;
	vector<int> elems;
};