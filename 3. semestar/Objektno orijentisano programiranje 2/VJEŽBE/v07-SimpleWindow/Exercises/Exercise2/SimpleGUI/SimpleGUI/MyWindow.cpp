#include "MyWindow.h"


MyWindow::MyWindow(Point xy, int w, int h, const string& title) :
	Graph_lib::Window(xy, w, h, title),
	radius(Point(IN_BOX_X_ALIGN, IN_BOX_Y_ALIGN), IN_BOX_X_OFFSET, IN_BOX_Y_OFFSET, "Circle Radius"),
	rectWidth(Point(IN_BOX_X_ALIGN, IN_BOX_Y_ALIGN), IN_BOX_X_OFFSET, IN_BOX_Y_OFFSET, "Rectangle Width"),
	rectHeight(Point(IN_BOX_X_ALIGN, IN_BOX_Y_ALIGN), IN_BOX_X_OFFSET, IN_BOX_Y_OFFSET, "Rectangle Height"),
	squareWidth(Point(IN_BOX_X_ALIGN, IN_BOX_Y_ALIGN), IN_BOX_X_OFFSET, IN_BOX_Y_OFFSET, "Square Width"),
	circleArea(Point(IN_BOX_X_ALIGN, IN_BOX_Y_ALIGN), IN_BOX_X_OFFSET, IN_BOX_Y_OFFSET, "Circle Area"),
	rectArea(Point(IN_BOX_X_ALIGN, IN_BOX_Y_ALIGN), IN_BOX_X_OFFSET, IN_BOX_Y_OFFSET, "Rectangle Area"),
	squareArea(Point(IN_BOX_X_ALIGN, IN_BOX_Y_ALIGN), IN_BOX_X_OFFSET, IN_BOX_Y_OFFSET, "Square Area"),
	getAreaButton(Point(IN_BOX_X_ALIGN, IN_BOX_Y_ALIGN), IN_BOX_X_OFFSET, IN_BOX_Y_OFFSET, "Get Areas", cb_getAreaButton)
{
	attach(radius);
	attach(rectWidth);
	attach(rectHeight);
	attach(squareWidth);
	attach(circleArea);
	attach(rectArea);
	attach(squareArea);
	attach(getAreaButton);
}



MyWindow::~MyWindow(void)
{
}

bool MyWindow::wait_for_button()
{
	show();
	Fl::run();
	return true;
}


void MyWindow::cb_getAreaButton(Address, Address pw)
{
	reference_to<MyWindow>(pw).getAreaButtonHandler();
}


void MyWindow::getAreaButtonHandler()
{

	double r = stod(radius.get_string());
	double w = stod(rectWidth.get_string());
	double h = stod(rectHeight.get_string());
	double a = stod(squareWidth.get_string());
	circleArea.put(to_string(r * r * 3.1415));
	rectArea.put(to_string(w * h));
	squareArea.put(to_string(a * a));
}
