#pragma once

class Complex {

public:
	Complex();
	Complex(double x, double y);
	~Complex();

	double getReal();
	double getImag();
	Complex add(Complex c);
	Complex sub(Complex c);
	Complex mul(Complex c);
	Complex mul(double s);
	Complex conj();

private:
	double a;
	double b;

};