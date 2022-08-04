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

void Complex::setReal(double r) {
	this->a = r;
}

void Complex::setImag(double i) {
	this->b = i;
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


Complex Complex::operator+(Complex c) {
	return this->add(c);
}

Complex Complex::operator-(Complex c) {
	return this->sub(c);
}

Complex Complex::operator*(Complex c) {
	return this->mul(c);
}
Complex Complex::operator*(double s) {
	return this->mul(s);
}

Complex Complex::operator~() {
	return this->conj();
}

std::istream& operator>>(std::istream& in, Complex& c) {
	double r;
	double i;
	in >> r >> i;
	c.setReal(r);
	c.setImag(i);
	return in;
}
std::ostream& operator<<(std::ostream& out, Complex c) {
	out << "(" << c.getReal() << ", " << c.getImag() << "i)";
	return out;
}


Complex operator*(double s, Complex& c) {
	return c.mul(s);
}