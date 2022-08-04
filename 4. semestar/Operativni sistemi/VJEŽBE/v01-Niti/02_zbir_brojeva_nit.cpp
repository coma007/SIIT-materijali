/* Napraviti program koji kreira jednu nit kojoj se prosledjuju dva cela broja
 * a i b. U okviru niti sabrati brojeve i ispisati njihov zbir
 */

#include <iostream>
#include <thread>

using namespace std;

void saberi(int a, int b) {
	cout << "Rezultat: " << a + b << endl; 
}

int main() {
	thread t(saberi, 2, 3);
	t.join();
	return 0;
}
