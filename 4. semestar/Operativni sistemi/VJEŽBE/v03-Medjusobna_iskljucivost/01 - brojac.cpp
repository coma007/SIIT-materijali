/* Napraviti konkurentni program koji sadrzi main funkciju i 2 niti. Obe niti
 * pristupaju istoj celobrojnoj promenljivoj brojac, koja inicijalno ima
 * vrednost 0.
 * Prva nit 1000000 puta uvecava vrednost brojaca.
 * Druga nit isti broj puta smanjuje vrednost brojaca.
 *
 * Ukoliko je program ispravno napisan, na kraju programa vrednost brojaca mora
 * biti 0.
 */

#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

int brojac = 0;
int iteracije = 100000000;
mutex m;

void uvecaj() {
	for (int i = 0; i < iteracije; i++) {
 		m.lock();
		brojac++;
		m.unlock();
	}
}

void umanji() { 
	for (int i = 0; i < iteracije; i++) {
		m.lock();
		brojac--;
		m.unlock();
	}
}

int main() {
	thread t1(uvecaj);
	thread t2(umanji);
	t1.join(); t2.join();
	cout << "Brojac: " << brojac;	
}



