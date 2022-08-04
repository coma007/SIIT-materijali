/* Napraviti konkurentni program koji određuje najbližu tačku kružnici (iz
 * velikog vektora tačaka - npr 100000000 elemenata).
 *
 * Program realizovati uz pomoć 2 klase:
 *
 * 1) Klasa Closest_point modelira najbližu tačku kružnici.
 * Interfejs klase sadrži sledeće metode:
 *
 * class Closest_point {
 *     void test_and_set(const Point& p, double d);
 *     friend ostream& operator<<(ostream& os, Closest_point& cp);
 * };
 *
 * Metoda test and set treba da proveri da li je prosleđena tačka p bliža od
 * trenutno najbliže tačke i da ako jeste postavi parametre nove najbliže tačke.
 * Operator služi za ispis koordinata najbliže tačke na ekran.
 *
 * 2) Klasa Circle modeluje kruznicu.
 * Interfejs klase sadrži sledeće metode:
 *
 * class Circle {
 *    double circle_distance(const Point& t);
 *    void find_closest(VPci p_begin, VPci p_end, Closest_point& cpoint);
 * };
 *
 * pri cemu je VPci je definisan kao
 *
 * typedef vector<Point>::const_iterator VPci;
 *
 * Metoda circle_distance treba da izračuna udaljenost tačke od kružnice.
 * Operator služi za prolazak kroz vektor tačaka i poređenje pojedinačnih tačaka
 * vektora sa trenutno najbližom tačkom (globalnom tačkom). Dato poređenje se
 * realizuje pozivanjem metode test_and_set na objektu najbliže tačke (cpoint).
 *
 * Kreirati jedan globalni objekat najbliže tačke.
 *
 * Kreirati 3 niti, pri cemu tela niti predstavlja data funkcija f
 *
 * void f(Circle& c, VPci p_begin, VPci p_end, Closest_point& cpoint) {
 *     c.find_closest(p_begin, p_end, cpoint);
 * }
 *
 * Svakoj niti se prosledjuje referenca na kruznicu koja se posmatra,1/3 vektora
 * tačaka kao i referenca na globalni objekat najbliže tačke. Nakon završetka
 * niti ispisati koodrdinate najbliže tačke.
 *
 * Napomena: konstruktore klasa Closest_point i Circle realizovati samostalno.
 * Kreirati veliki vektor tačaka (npr. 10000 elemenata) sa slučajnim vrednostima
 * koordinata tačaka (ne predalekim od kružnice).
 */

#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <math.h>
#include <random>

using namespace std;

struct Point {
	double x, y;
};

class Closest_point {
	double distance;
	bool set;
public:
	Point pt;
	mutex m;
	void test_and_set(const Point& p, double d) {
		unique_lock<mutex> l(m);
		if (d < distance || !set) {
			pt.x = p.x;
			pt.y = p.y;
			distance = d;
			set = true;
			return;		
		}		
	}
	friend ostream& operator<<(ostream& os, Closest_point& cp) {
		unique_lock<mutex> l(cp.m);		
		os << "(x,y) = (" << cp.pt.x << "," << cp.pt.y << ")" << endl; 	
		return os;
	}
};

typedef vector<Point>::const_iterator VPci; 

class Circle {
	Point center;
	double diameter;
	double circle_distance(const Point& t) {
		return abs(sqrt(pow((t.x-center.x),2) + pow((t.y-center.y),2))-diameter);
	}	
public:
	Circle(Point c, double d) : center(c), diameter(d) {}
	void find_closest(VPci p_begin, VPci p_end, Closest_point& cpoint) {
		for (; p_begin != p_end; p_begin++) {
			double distance = circle_distance(*p_begin);
			cpoint.test_and_set(*p_begin, distance);
		}
	}
};

void f(Circle& c, VPci p_begin, VPci p_end, Closest_point& cpoint) {
	c.find_closest(p_begin, p_end, cpoint);
}

int main() {

	Closest_point pt;
	Closest_point ptr;
	Circle c(Point{0,0}, 10);
	vector<Point> vp(100000);
	for (int i = 0; i < vp.size(); i++) {
		vp[i] = Point{(double)rand()/10000000, (double)rand()/10000000};
	}
	VPci first = vp.begin();
	VPci second = first + vp.size()/3;
	VPci third = second + vp.size()/3;
	thread t1(f, ref(c), first, second, ref(pt));
	thread t2(f, ref(c), second, third, ref(pt));
	thread t3(f, ref(c), third, vp.end(), ref(pt));
	thread t4(f, ref(c), first, vp.end(), ref(ptr));
	t1.join();
	t2.join();
	t3.join();
	t4.join();
	cout << pt;
	cout << ptr;
	return 0;
}


