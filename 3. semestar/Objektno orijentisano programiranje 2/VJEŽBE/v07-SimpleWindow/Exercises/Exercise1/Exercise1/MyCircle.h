#pragma once
#include "MyShape.h"

class MyCircle : public MyShape {
public:
	MyCircle();
	MyCircle(double r);
	~MyCircle();
	double getArea();

};
