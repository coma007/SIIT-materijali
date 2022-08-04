#include "MyCircle.h"


MyCircle::MyCircle(double r) : MyShape(r, r) {}

MyCircle::~MyCircle() {}

double MyCircle::getArea() {
	return x*y*3.1415;
}