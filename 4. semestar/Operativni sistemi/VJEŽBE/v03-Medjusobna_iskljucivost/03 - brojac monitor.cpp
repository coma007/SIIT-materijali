/* Napraviti konkurentni program koji modeluje klasu brojača.
 * Interfejs klase sadrži sledeće metode:
 *
 * class brojac {
 * public:
 *     void inc();
 *     void dec();
 *     friend ostream& operator<<(ostream& , brojac& );
 * };
 *
 * Metode inc i dec povećavaju, odnosno smanjuju vrednost brojača za 1. Operator
 * << služi za ispis brojača na ekran. Klasa mora biti thread-safe (da garantuje
 * ispravan rad i ako se objektu klase pristupa iz razlicitih niti).
 *
 * Kreirati jednu instancu date klase kojoj pristupaju 2 niti.
 *
 * Jedna nit poziva metodu uvećavanja brojača 1000000 puta, a druga metodu
 * smanjivanja brojača 1000000 puta.
 *
 * Na kraju programa ispisati konačnu vrednost brojača.
 */

#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

int iters = 10000000;

class brojac {
public:
	mutex m;
	int val = 0;
	void inc() {unique_lock<mutex> l(m); val++;}
	void dec() {unique_lock<mutex> l(m); val--;}
	friend ostream& operator<<(ostream& o, brojac& b) {
		o << b.val;
	}
};

void incT(brojac& b) {
	for (int i = 0; i != iters; i++)
	b.inc();
}

void decT(brojac& b) {
	for (int i = 0; i != iters; i++)
	b.dec();
}

int main() {
	brojac b;
	thread t1(incT, ref(b));
	thread t2(decT, ref(b));
	t1.join(); t2.join();
	cout << b;
}
