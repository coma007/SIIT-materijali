#include "MySquare.h"

MySquare::MySquare() : MyRectangle(0, 0) {};
MySquare::MySquare(double a) : MyRectangle(a, a) {};

MySquare::~MySquare() {}

double MySquare::getArea() {
	return x*x;
}