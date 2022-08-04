/* Napraviti konkurentni program  (koristeći funkciju f()) koji sabira
 * korespodentne elemente kontejnera  a i b, a rezultat smešta u vektor zbir.
 *
 * Dato je telo niti:
 *
 * void f(ci a_begin, ci a_end, ci b_begin, vector<double>::iterator sum_begin);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 *
 * Program optimizovati za procesor sa 2 jezgra.
 *
 * Napomene: Podrazumeva se da su kontejneri a i b iste dužine.
 */

#include <iostream>
#include <thread>
#include <vector>

using namespace std;
typedef vector<double>::const_iterator ci;

void f(ci a_begin, ci a_end, ci b_begin, vector<double>::iterator sum_begin) {
	for (; a_begin != a_end; a_begin++, b_begin++, sum_begin++) {
		*sum_begin = *a_begin + *b_begin;
	}
}

int main() {
	vector<double> a = {1, 2, 3, 4, 5};
	vector<double> b = {1, 2, 3, 4, 5};
	int size = a.size();
	vector<double> sum(size);
	thread t1(f, a.begin(),
	 	  a.begin() + size/2,
	 	  b.begin(), sum.begin());
	thread t2(f, a.begin() + size/2,
		  a.end(), b.begin() + size/2,
		  sum.begin()+size/2);
	t1.join();
	t2.join();
	for (int i = 0; i != size; i++) {
		cout << "sum[" << i << "] = " << sum[i] << endl;
	}
}
