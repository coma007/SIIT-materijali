/* Sabrati korespodentne elemente vektora a i b, a zbirove smestiti na
 * odgovarajuce pozicije vektora c. Obezbediti da svako sabiranje obavlja
 * posebna nit.
 */


#include <iostream>
#include <thread>
#include <vector>

using namespace std;

typedef vector<double>::const_iterator ci;

void f(ci a_pos, ci b_pos, vector<double>::iterator c_pos) {
	*c_pos = *a_pos + *b_pos; 
}

int main() {
	vector<double> a = {1, 2, 3, 4, 5, 6, 7};
	ci a_pos = a.begin();
	vector<double> b = {1, 2, 3, 4, 5, 6 ,7};
	ci b_pos = b.begin();
	int size = a.size();
	vector<double> c(size);
	vector<double>::iterator c_pos = c.begin();
	thread t[size];
	for (int i = 0; i != size; i++) {
		t[i] = thread(f, a_pos, b_pos, c_pos);
		a_pos++; b_pos++; c_pos++;
	}
	for (int i = 0; i != size; i++) {
		t[i].join();
	}
	for (int i = 0; i != size; i++) {
		cout << "c[" << i << "] = " << c[i] << endl;
}
	return 0;
}
