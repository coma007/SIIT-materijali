/* Napraviti konkurentni program koji pita korisnika koliko niti da stvori, a
 * zatim stvara zadati broj niti. Pri instanciranju nit dobija redni broj pod
 * kojim je stvorena. Svaka nit ispisuje svoj redni broj i svoj identifikator.
 */

#include <iostream>
#include <thread>

using namespace std;

void nit(int rbr) {
	cout << "Ja sam nit " << rbr << endl;
}

int main() {
	cout << "Unesi broj niti : ";
	int broj;
	cin >> broj;
	thread t[broj];
	for (int i = 0; i != broj; i++) {
		t[i] = thread(nit, i);
	}
	for (int i = 0; i != broj; i++) {
		t[i].join();
	}
}
