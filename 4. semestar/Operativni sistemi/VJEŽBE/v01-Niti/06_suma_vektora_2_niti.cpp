/* Napraviti konkrentni program koji izračunava sumu svih elemenata vektora,
 * koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 *
 * Podeliti racunanje sume na 2 dela tako da prvu polovinu vektora sumira prva
 * nit, a drugu polovinu druga nit.
 *
 * Napomena: ovakva optimizacija sumiranja je znacajna kada se radi na
 * dvojezgarnom procesoru za vektore velike duzine.
 */

#include <iostream>
#include <vector>
#include <thread>

using namespace std;
typedef vector<double>::const_iterator ci;

void f(ci begin, ci end, double& zbir) {
	for (; begin != end; begin++) {
		zbir += *begin;	
	}
}

int main() {
	vector<double> v = {1, 2, 3, 4, 5, 6};
	double zbir1, zbir2;
	thread t1(f, v.begin(), v.begin() + v.size()/2, ref(zbir1));
	thread t2(f, v.begin() + v.size()/2, v.end(), ref(zbir2));
	t1.join();
	t2.join();
	cout << zbir1 + zbir2;
	return 0;
}
