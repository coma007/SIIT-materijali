#pragma once
#include <iostream>

class Complex {

public:
	Complex();
	Complex(double x, double y);
	~Complex();

	double getReal();
	double getImag();

	void setReal(double r);
	void setImag(double i);

	Complex add(Complex c);
	Complex sub(Complex c);
	Complex mul(Complex c);
	Complex mul(double s);
	Complex conj();

	Complex operator+(Complex c);
	Complex operator-(Complex c);
	Complex operator*(Complex c);
	Complex operator*(double s);
	Complex operator~();

	// moze da pristupi svim atributima ove klase, ali u sustini ne pripada ovoj klasi
	// odnosno moci ce da se pise bez Complex::, a ima pristup svim atributima
	friend std::istream& operator>>(std::istream& in, Complex& c);
	friend std::ostream& operator<<(std::ostream& out, Complex c);


private:
	double a;
	double b;

};

Complex operator*(double s, Complex& c);