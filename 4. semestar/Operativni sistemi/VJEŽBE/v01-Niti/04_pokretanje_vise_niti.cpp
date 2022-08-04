/* Napraviti konkurentni program koji kreira 5 niti od kojih svaka izvrsava isti
 * kod (svaka nit ima isto telo niti).
 * Svaka nit dobija svoj redni broj prilikom kreiranja.
 * U telu niti svaka nit treba da ispise svoj redni broj.
 */

#include <iostream>
#include <thread>

using namespace std;

void ispis(int rbr) {
	cout << "Nit broj: " << rbr << endl;
}

int main() {
	thread t1(ispis, 1), t2(ispis, 2),
	t3(ispis, 3), t4(ispis, 4), t5(ispis, 5);
	t2.join(); t1.join(); t3.join(); t4.join(); t5.join();
}
