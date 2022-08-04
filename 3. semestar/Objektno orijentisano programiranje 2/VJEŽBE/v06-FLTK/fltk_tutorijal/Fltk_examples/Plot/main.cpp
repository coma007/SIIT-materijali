#include "Simple_window.h"
#include "Graph.h"

using namespace Graph_lib;

int main(int argc, char **argv)
{
	// Canvas#1
	Point pt(100,100);
	Simple_window win(pt, 600, 400, "Canvas#1");
	win.wait_for_button();

	// Canvas#2
	Axis xa(Axis::x,			// Axis::x means horizontal
		Point(20, 300),			// starting at 20, 300
		400,					// 280 pixels long
		20,						// 10 notches
		"x axis");				// label of the axis

	win.attach(xa);
	win.set_label("Canvas#2");
	win.wait_for_button();

	// Canvas#3
	Axis ya(Axis::y,
		Point(20, 300), 
		250, 
		20, 
		"y axis");
	ya.set_color(Color::cyan);
	ya.label.set_color(Color::dark_green);

	win.attach(ya);
	win.set_label("Canvas#3");
	win.wait_for_button();

	// Canvas#4
	Function sine(sin,			// sine curve
		0, 10,					// range [0:100)
		Point(20, 300),			// starting point (0,0) at (20,300)
		1000,					// using 1000 points
		50, 50);				// scale x and y values by 50

	sine.set_style(Line_style::dashdot);
	sine.set_color(Color::dark_red);
	win.attach(sine);
	win.set_label("Canvas#4");
	win.wait_for_button();

	return 0;
}
