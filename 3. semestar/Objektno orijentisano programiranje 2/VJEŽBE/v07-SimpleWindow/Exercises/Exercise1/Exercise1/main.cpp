#include "std_lib_facilities.h"
#include "Shapes.h"

void main ()
{
	vector<MyShape*> shapes(5);

	MyCircle circle1(15.0);
	MyCircle circle2(2.3);
	MyRectangle rect1(34.0,2.0);
	MyRectangle rect2(5.61,7.92);
	MySquare sq(3.33);

	shapes[0] = &circle1; 
	shapes[1] = &rect1; 
	shapes[2] = &circle2;
	shapes[3] = &sq;
	shapes[4] = &rect2;

	for (int k=0; k<5; k++)
		cout << "Area is " << shapes[k]->getArea() << endl;
	
	return;
}
