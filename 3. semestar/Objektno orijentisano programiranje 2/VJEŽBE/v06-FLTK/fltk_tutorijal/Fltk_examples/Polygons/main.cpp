#include "Simple_window.h"
#include "Graph.h"

using namespace Graph_lib;

int main(int argc, char **argv)
{
	Point pt(100,100);

	Simple_window win(pt, 600, 400, "Canvas");

	Graph_lib::Polygon triangle;
	triangle.add(Point(300,200));
	triangle.add(Point(350,100));
	triangle.add(Point(400,200));
	triangle.set_color(Color::green);

	win.attach(triangle);
	win.wait_for_button();

	win.detach(triangle);

	Graph_lib::Rectangle rect(Point(200,200), 100, 50);
	rect.set_color(Color::dark_yellow);

	win.attach(rect);
	win.wait_for_button();

	rect.set_fill_color(Color::yellow);
	win.wait_for_button();

	win.detach(rect);
	Closed_polyline polygon;
	polygon.add(Point(50, 50));
	polygon.add(Point(100, 50));
	polygon.add(Point(125, 75));
	polygon.add(Point(75, 100));
	polygon.add(Point(25, 75));

	win.attach(polygon);
	win.wait_for_button();

	polygon.move(50, 0);
	polygon.set_style(Line_style(Line_style::dash, 5));

	win.wait_for_button();

	Text t(Point(150, 150), "Hello, graphical world!");
	t.set_font(Font::helvetica_bold);
	t.set_font_size(20);

	Circle c(Point(300,200), 50);
	Mark m(Point(300,200),'x');		// circle center

	win.attach(t);
	win.attach(c);
	win.attach(m);
	win.wait_for_button();

	win.detach(t);
	win.detach(polygon);
	win.detach(c);
	win.detach(m);

	win.resize(256,256);
	Image img(Point(0,0), "img.jpg");
	win.attach(img);
	win.wait_for_button();

	return 0;
}
