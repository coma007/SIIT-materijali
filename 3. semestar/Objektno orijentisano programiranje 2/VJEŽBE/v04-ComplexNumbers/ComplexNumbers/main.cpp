#include <iostream>
#include "myComplex.h"

using namespace std;

int main() {

	Complex a(3.0, 4.0); // initialize to (3, 4i)
	Complex b(5.0, 7.0); // initialize to (5, 7i)
	Complex c;
	cout << "a (" << a.getReal() << ", " << a.getImag() << "i) " << endl;
	cout << "b (" << b.getReal() << ", " << b.getImag() << "i) " << endl;
	c = a.add(b);
	cout << "a + b = (" << c.getReal() << ", " << c.getImag() << "i) " << endl;
	c = a.sub(b);
	cout << "a - b = (" << c.getReal() << ", " << c.getImag() << "i) " << endl;
	c = a.mul(b);
	cout << "a * b = (" << c.getReal() << ", " << c.getImag() << "i) " << endl;
	c = a.conj();
	cout << "~a = (" << c.getReal() << ", " << c.getImag() << "i) " << endl;
	cout << "Done!" << endl;

	return 0;

}