#pragma once


class MyShape {
protected:
	double x, y;
public:
	MyShape();
	MyShape(double a, double b);
	~MyShape();
	virtual double getArea() = 0;

};
