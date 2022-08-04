#include "Simple_window.h"
#include "Graph.h"

int main(int argc, char **argv)
{
	using namespace Graph_lib;

	Point pt(100,100);

	Simple_window win(pt, 600, 400, "Canvas");

	win.wait_for_button();

	return 0;
}
