#include <iostream>

using namespace std;

class Shape
{
public:
	~Shape();
	void draw();
};

class Circle : public Shape
{
public:
	~Circle();
	void draw();
};

Shape::~Shape()
{
	cout << "Shape destructor" << endl;
}

void Shape::draw()
{
	cout << "Shape::draw" << endl;
}

Circle::~Circle()
{
	cout << "Circle destructor" << endl;
}

void Circle::draw()
{
	cout << "Circle::draw" << endl;
}


int main(int argc, char **argv)
{
	Shape *shape = new Circle;
	shape->draw();
	delete shape;
	return 0;
}
