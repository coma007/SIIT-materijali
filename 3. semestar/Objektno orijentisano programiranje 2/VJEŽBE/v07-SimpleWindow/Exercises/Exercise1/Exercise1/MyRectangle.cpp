#include "MyRectangle.h"

MyRectangle::MyRectangle() : MyShape(0, 0) {}
MyRectangle::MyRectangle(double a, double b) : MyShape(a, b) {};

MyRectangle::~MyRectangle() {}

double MyRectangle::getArea() {
	return x * y;
}