/* Definisati klasu parking koja modeluje parking prostor kapaciteta N mesta.
 * Kapacitet parkinga proslediti kao argument konstruktoru, pri instanciranju
 * deljene promenljive.
 *
 * Klasa parking ima operacije:
 *
 *     void parking::udji();
 *     void parking::izadji();
 *
 * Automobili koji dolaze na parking su predstavljeni nitima. Za ulazak na
 * parking, automobil poziva metodu udji(). Za izlazak sa parkinga, automobil
 * poziva metodu izadji(). Automobil se na parkingu zadrzava 3 sekunde.
 *
 * Pri ulasku, ukoliko su sva parking mesta zauzeta, automobil mora da saceka da
 * se neko parking mesto oslobodi.
 */
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

class parking {
  private:
	int br_mjesta;
	int br_slobodnih;
	mutex mx;
	condition_variable cv;
  public:
	parking(int N) : br_mjesta(N), br_slobodnih(N) {};
	void udji() {
		unique_lock<mutex> l(mx);
		while (br_slobodnih == 0) cv.wait(l);
		br_slobodnih--;
	}
	void izadji() {
		unique_lock<mutex> l(mx);
		br_slobodnih++;
		cv.notify_one();
	}
};

mutex m;
void automobil(parking& p) {
   p.udji();
   { unique_lock<mutex> l(m);
      cout << "Automobil " << this_thread::get_id() << " usao na parking." << endl;
   }
   this_thread::sleep_for(chrono::seconds(3));
   p.izadji();
   { unique_lock<mutex> l(m);
      cout << "Automobil " << this_thread::get_id() << " izasao sa parkinga." << endl;
   }
}

int main() {
	int KAPACITET = 5;
	int BROJ_AUTOMOBILA = 10;
	thread t[BROJ_AUTOMOBILA];
	parking p(KAPACITET);
	for (int i = 0; i < BROJ_AUTOMOBILA; i++) {
		t[i] = thread(automobil, ref(p));
	}
	for (int i = 0; i < BROJ_AUTOMOBILA; i++) {
		t[i].join();
	}
	
}
