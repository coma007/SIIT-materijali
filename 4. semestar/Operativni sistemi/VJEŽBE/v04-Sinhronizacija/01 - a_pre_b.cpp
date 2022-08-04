/* Napraviti konkurentni program sa dve niti.
 * Nit a ispisuje: "Ja sam nit a."
 * Nit b ispisuje: "Ja sam nit b."
 * Obezbediti da se uvek izvrsi prvo nit a.
 */

#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

mutex m;
condition_variable cv;
bool a_gotov = false;

void a() {
	unique_lock<mutex> l(m);
	cout << "Ja sam nit a." << endl;
	a_gotov = true;
	cv.notify_one();
}

void b() {
	unique_lock<mutex> l(m);
	while (!a_gotov) cv.wait(l);
	cout << "Ja sam nit b." << endl;
}

int main() {
	thread ta(a), tb(b);
	ta.join(); tb.join();
	return 0;
}
