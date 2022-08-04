/* Napisati konkurentni program koji koristi STL kontejner <map>. U main-u
 * inicijalizovati mapu tako da sadrzi 10 elemenata pri cemu je kljuc broj od
 * 1-10 a vrednost id niti main.
 * 
 * Kreirati 10 niti klasom thread. Svakoj niti se prosleduje njen redni broj
 * prilikom stvaranja i referenca na mapu. Svaka nit u mapi treba upise svoj id
 * na element kojem je kljuc redni broj date niti (1-10).
 * 
 * Na kraju programa iz mape ispisati id-eve niti u obrnutom redosledu rednog
 * broja niti.
 */

#include <iostream>
#include <thread>
#include <map>

using namespace std;


typedef map<int, thread::id>::reverse_iterator rom; 
int BROJ_NITI = 10;

void f(int rbr, map<int, thread::id>& m) {
	m[rbr] = this_thread::get_id();
}

int main() {
	map<int, thread::id> ids;
	for (int i =0; i != BROJ_NITI; i++) {
		ids[i] = this_thread::get_id();
	}
	thread t[BROJ_NITI];
	for (int i = 0; i != BROJ_NITI; i++) {
		t[i] = thread(f, i, ref(ids));
	}
	for (int i = 0; i != BROJ_NITI; i++) {
		t[i].join();
	}
	for (rom r = ids.rbegin(); r != ids.rend(); r++) {
		cout << "ids[" << r->first << "] = " << r->second << endl;
	}
	return 0;
}
