#include "Simple_window.h"
#include "Graph.h"

using namespace Graph_lib;


struct Box : Shape {

	Box(Point p, int ww, int hh, Simple_window wind) : width(ww), height(hh), win(&wind) {
		add(Point(p.x - ww, p.y - hh));
	}

	void draw_lines() const
	{
			fl_line(point(0).x + width / 4, point(0).y, point(0).x + (3. / 4.) * width, point(0).y);
			fl_line(point(0).x + width / 4, point(0).y + height, point(0).x + (3. / 4.) * width, point(0).y + height);
			fl_line(point(0).x, point(0).y + height / 4, point(0).x, point(0).y + (3. / 4.) * height);
			fl_line(point(0).x + width, point(0).y + height / 4, point(0).x + width, point(0).y + (3. / 4.) * height);

			fl_arc(point(0).x, point(0).y, width / 2, height / 2, 90, 180);
			fl_arc(point(0).x + width / 2, point(0).y, width / 2, height / 2, 0, 90);
			fl_arc(point(0).x + width / 2, point(0).y + height / 2, width / 2, height / 2, 270, 0);
			fl_arc(point(0).x, point(0).y + height / 2, width / 2, height / 2, 180, 270);
	}

	private:
		int width;
		int height;
		Simple_window* win;
};


int main()
{
	Simple_window* win = new Simple_window(Point(100, 100), 1000, 700, "Canvas");
	win->wait_for_button();
	Box b(Point(150, 150), 100, 50, *win);
	win->attach(b);
	win->wait_for_button();

}

