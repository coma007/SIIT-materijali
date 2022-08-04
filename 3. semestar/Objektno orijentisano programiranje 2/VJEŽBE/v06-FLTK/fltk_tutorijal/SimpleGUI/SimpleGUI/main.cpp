#include "MyWindow.h"

int main(int argc, char **argv)
{
	MyWindow win(Point(100,200), 300, 60, "App");
	win.wait_for_button();
	return 0;
}