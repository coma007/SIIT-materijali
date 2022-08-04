/* Napraviti sekvencijalni program koji izračunava sumu svih elemenata vektora
 * sekvencijalno, koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 */

#include <iostream>
#include <vector>

using namespace std;

typedef vector<double>::const_iterator ci;

void f(ci begin, ci end, double& zbir) {
 	for (ci i = begin; i != end; i++) {
		zbir += *i;
	}
}

int main() {
	vector<double> v = {1, 2, 3, 4, 5, 6, 7};
	double zbir;
	f(v.begin(), v.end(), zbir);
	cout << zbir << endl;
}
