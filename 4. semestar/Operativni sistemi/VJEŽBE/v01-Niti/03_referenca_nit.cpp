/* Napisati konkurentni program koji stvara jednu nit.
 * Nit od glavnog programa kao parametar dobija ceo broj i ima zadatak da uveca
 * vrednost broja za 1.
 *
 * Ispisati vrednost broja nakon zavrsetka rada niti
 */

#include <iostream>
#include <thread>

using namespace std;

void inkrement(int &broj) {
	broj++;
}

int main() {
	int a = 5;
	thread t(inkrement, ref(a));
	t.join();
	cout << a;
	return 0;
}
