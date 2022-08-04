#include "SimWindow.h"
#include "Graph.h"

using namespace Graph_lib;

int main(int argc, char **argv)
{
	SimWindow win(Point(0,0), WINDOW_W, WINDOW_H, "Simulator");

	// create X axis and Y axis
	// add axes to the window
	// use constants defined in SimWindow.h to align axes
	Axis x(Axis::x, Point(HOR_OFFSET, WINDOW_H / 2), X_AXIS_SIZE, NUM_OF_NOTCH_X, "x osa");
	x.set_color(Color::black);
	win.attach(x);
	Axis y(Axis::y, Point(WINDOW_W / 2, WINDOW_H - VER_OFFSET), Y_AXIS_SIZE, NUM_OF_NOTCH_Y, "y osa");
	y.set_color(Color::black);
	win.attach(y);

	win.simulate();
	return 0;
}
