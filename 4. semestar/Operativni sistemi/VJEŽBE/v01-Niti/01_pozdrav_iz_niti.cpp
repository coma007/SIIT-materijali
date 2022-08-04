/* Napraviti program koji kreira jednu nit i u okviru nje ispisuje proizvoljnu
 * recenicu.
 */
#include <iostream>
#include <thread>

using namespace std;

void stampa() {
	cout << "Hello, world !" << endl;
}

int main() {
	thread t(stampa);
	t.join();
	return 0;
}
