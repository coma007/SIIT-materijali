#include "MyWindow.h"


void main()
{
	MyWindow win(Point(0,0), WINDOW_W, WINDOW_H, "App");
	win.wait_for_button();
	return;
}