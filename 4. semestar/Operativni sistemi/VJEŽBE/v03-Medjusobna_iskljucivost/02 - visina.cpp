/* Napraviti konkurentni program sa 2 niti koje imaju isto telo niti. Svaka nit
 * najpre trazi od korisnika da unese svoju visinu. Nakon unosa, nit ispisuje
 * unetu vrednost na terminal.
 *
 * Sinhronizovati pristup terminalu kao deljenom resursu. Kada jedna nit stupi u
 * interakciju sa korisnikom, ne sme biti prekinuta dok se ne zavrsi kompletna
 * interakcija (i unos i ispis).
 */

#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

mutex m;

void f() {
	int visina;
	m.lock();
	cout << "Unesite visinu : ";
	cin >> visina;
	cout << "Vasa visina je : " << visina << endl;
	m.unlock();
}

int main() {
	thread t1(f);
	thread t2(f);
	t1.join(); t2.join();
	return 0;
}
