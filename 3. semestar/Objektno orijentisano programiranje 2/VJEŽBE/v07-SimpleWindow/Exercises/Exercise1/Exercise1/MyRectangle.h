#pragma once
#include "MyShape.h"

class MyRectangle : public MyShape {
public:
	MyRectangle();
	MyRectangle(double a, double b);
	~MyRectangle();
	double getArea();

}; 
	

