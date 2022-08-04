/* Napraviti konkrentni program koji izračunava sumu svih elemenata vektora,
 * koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 *
 * Podeliti racunanje sume na N delova tako svaka nit sabira duzina vektora/broj
 * niti elemenata vektora.
 */

#include <iostream>
#include <vector>
#include <thread>

using namespace std;
typedef vector<double>::const_iterator ci;

const int BROJ_NITI = 7;

void f(ci begin, ci end, double& zbir) {
	for (; begin != end; begin++) {
		zbir += *begin;
	}
}

int main() {
	vector<double> v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	thread t[BROJ_NITI];	
	double zbir[BROJ_NITI];
	ci begin = v.begin();
	ci end = v.begin() + v.size() / BROJ_NITI;
	for (int i = 0; i != BROJ_NITI - 1 ; i++) {
		t[i] = thread(f, begin, end, ref(zbir[i]));
		begin = end;
		end = end + v.size() / BROJ_NITI;
	}
	t[BROJ_NITI - 1] = thread(f, begin, v.end(), ref(zbir[BROJ_NITI-1]));
	for (int i = 0; i != BROJ_NITI; i++) {
		t[i].join();
	}
	int total;
	for (int i = 0; i != BROJ_NITI; i++) {
		total += zbir[i];
	}	
	cout << total << endl;
	return 0;
}
