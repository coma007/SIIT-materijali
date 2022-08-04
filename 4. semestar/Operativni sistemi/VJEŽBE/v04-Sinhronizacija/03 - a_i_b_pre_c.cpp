/* Napraviti konkurentni program sa tri niti.
 * Nit a ispisuje: "Ja sam nit a."
 * Nit b ispisuje: "Ja sam nit b."
 * Nit c ispisuje: "Ja sam nit c."
 * Obezbediti da se niti a i b, uvek izvrse pre niti c.
 */

#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

class kontroler {
private:
	const int cekanje;
	int proslo;
	mutex m;
	condition_variable cv;
public:
	kontroler(int c) : cekanje(c), proslo(0) {}
	void zavrsio() {
		unique_lock<mutex> l(m);
		if (++proslo == cekanje) {
			cv.notify_all();
		}	
	}
	void cekam() {
		unique_lock<mutex> l(m);
		while (proslo != cekanje) {
			cv.wait(l);
		}
	}
};

mutex mx;
void a(kontroler &k) {
	unique_lock<mutex> l(mx);
	cout << "Ja sam nit a." << endl;
	k.zavrsio();
}

void b(kontroler &k) {
	unique_lock<mutex> l(mx);
	cout << "Ja sam nit b." << endl;
	k.zavrsio();
}

void c(kontroler &k) {
	k.cekam();
	unique_lock<mutex> l(mx);
	cout << "Ja sam nit c." << endl;
}

int main() {
	kontroler k(2);
	thread ta(a, ref(k)), tb(b, ref(k)), tc(c, ref(k));
	ta.join(); tb.join(); tc.join();
}
