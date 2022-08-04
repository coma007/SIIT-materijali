#pragma once
#include "MyRectangle.h"

class MySquare : public MyRectangle {
public:
	MySquare();
	MySquare(double a);
	~MySquare();
	double getArea();

};
