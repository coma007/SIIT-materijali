#include "myComplex.h"
#include <iostream>

using namespace std;

Complex::Complex() : a(0), b(0) {}

Complex::Complex(double x, double y) : a(x), b(y) {}

Complex::~Complex() {}

double Complex::getReal() {
	return this->a;
}

double Complex::getImag() {
	return this->b;
}

Complex Complex::add(Complex c) {
	double real = this->a + c.getReal();
	double imaginary = this->b + c.getImag();
	return Complex(real, imaginary);
}

Complex Complex::sub(Complex c) {
	double real = this->a - c.getReal();
	double imaginary = this->b - c.getImag();
	return Complex(real, imaginary);
}

Complex Complex::mul(Complex c) {
	double real = (this->a + c.getReal()) - (this->b + c.getImag());
	double imaginary = (this->a * c.getImag()) + (this->b * c.getReal());
	return Complex(real, imaginary);
}

Complex Complex::mul(double c) {
	double real = this->a * c;
	double imaginary = this->b * c;
	return Complex(real, imaginary);
}

Complex Complex::conj() {
	return Complex(this->a, -this->b);
}
