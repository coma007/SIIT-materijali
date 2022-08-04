/* Napraviti konkurentni program za transliranje 2D poligona u ravni za 
 * definisani pomeraj po x i y koordinati. Poligon predstaviti kao skup tacaka
 * definisan u STL kontejneru.
 * 
 * Na pocetku programa pitati korisnika da unese pomeraj za x koordinatu i y
 * koordinatu.
 * 
 * Stvoriti 2 niti. Jedna nit treba da izvrsi translaciju svih x koordinata 
 * tacaka za definisani pomeraj, a druga nit translaciju y koordinata.
 * 
 * Na kraju programa ispisati tacke transliranog poligona.
 */


#include <iostream>
#include <thread>
#include <vector>

using namespace std;

const int dx = 20;
const int dy = 10;

struct Point {
	double x;
	double y;
	Point(int xp, int yp) : x(xp), y(yp) {}
	void toString() {
		cout << "(x=" << x << ",y=" << y << ")" << endl;
	}
};

typedef vector<Point>::iterator it;

void translate(it begin, it end, double d, bool xCoor) {

	for (; begin != end; begin++) {
		if (xCoor) {
			begin->x += d;
		}
		else {
			begin->y += d;
		}
	}
}

int main() {
	vector<Point> points = {Point(0, 0), Point(1, 1), Point(2, 2)};
	thread tx = thread(translate, points.begin(), points.end(), dx, true);
	thread ty = thread(translate, points.begin(), points.end(), dy, false);
	tx.join();
	ty.join();
	for (Point pt : points) {
		pt.toString();
	}						
}
