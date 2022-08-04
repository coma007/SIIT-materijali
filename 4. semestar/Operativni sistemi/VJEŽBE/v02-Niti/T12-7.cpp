/* Napraviti program za evidenciju identifikatora niti. U programu definisati
 * STL kontejner sa 5 elemenata (isto toliko ce biti i niti). Elementi
 * kontejnera su objekti koji predstavljaju identifikatore niti. Svaka nit treba
 * u dati STL kontejner da upise svoj identifikator i to u odgovarajuci element.
 *
 * Dakle, prva nit upisuje svoj identifikator u prvi element vektora, druga nit
 * u drugi element i tako redom. Kada se sve niti zavrse, potrebno je ispisati
 * identifikatore uskladistene u STL kontejneru.
 */

#include <iostream>
#include <thread>
#include <vector>

using namespace std;

int BROJ_NITI = 10;

void f(vector<thread::id>& ids, int pos) {
	ids[pos] = this_thread::get_id();
}

int main() {
	vector<thread::id> ids(BROJ_NITI);
	thread t[BROJ_NITI];
	for (int i = 0; i != BROJ_NITI; i++) {
		t[i] = thread(f, ref(ids), i);
	}
	for (int i = 0; i != BROJ_NITI; i++) {
		t[i].join();
	}
	for (int i = 0; i != BROJ_NITI; i++) {
		cout << "ids[" << i << "] = " << ids[i] << endl;
	}
}
