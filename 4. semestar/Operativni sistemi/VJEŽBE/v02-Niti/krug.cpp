/* Napisati program koji proverava koje se od zadatih tacaka nalaze u/na 
 * kruznici, a koje su van kruznice.
 * Tacke se nalaze u vektoru points:
 * 
 * struct Point { double x, y; };
 * vector<Point> points;
 * 
 * Definisati klasu:
 * 
 * class Circle {
 *   ...
 * public:
 *   Circle(const Point& t, const double r_);
 *   void check(const vector<Point> p, vector<bool>& belong);
 * };
 * 
 * Objekt tipa Circle, za svaku tacku iz vektora, izracunava da li se ona nalazi:
 *     - u krugu (ili na kruznici)
 *         + korespodentni element vektora belong dobija vrednost true ili
 *     - van kruga
 *         + korespodentni element vektora belong dobija vrednost false.
 * 
 * Stvoriti nit koja poziva funkciju check nad objektom klase Circle.
 */

#include <iostream>
#include <thread>
#include <vector>
#include <math.h>

using namespace std;

struct Point {double x, y;};

class Circle {
	Point center;
	double diameter;
public:
	Circle (const Point& t, const double r_) : center(t), diameter(r_) {}
	void check(const vector<Point> p, vector<bool>& belong) {
		int d = 0;
		for (int i = 0; i != belong.size(); i++) {
			d = sqrt(pow((p[i].x - center.x), 2) + pow((p[i].y - center.y), 2));
			if (d > diameter) {
				belong[i] = false;
			}
			else {
				belong[i] = true;
			}
		}
	} 
};

void f(vector<Point>& p, Circle& c, vector<bool>& belong) {
	c.check(p, belong);
}


int main() {
	vector<Point> points = {Point{1, 2}, Point{2, 3}, Point{3, 4}};
	vector<bool> belong(points.size(), false);
	Circle c(Point{0, 0}, 3);
	thread t(f, ref(points), ref(c), ref(belong));
	t.join();
	for (int i = 0; i != points.size(); i++) {
		cout << "(x=" << points[i].x << ",y=" << points[i].y << "): " << belong[i] << endl;
	}
	return 0;
}








