/*
	Modelovati koriscenje zaletista na atletskom mitingu.
	Isto zaletiste koriste dve discipline: skok u dalj i bacanje koplja.
	Zaletiste ne mogu istovremeno da koriste dva takmicara.
	Discipline se naizmenicno smenjuju na zaletistu (jedan skakac u dalj, pa jedan bacac koplja i tako redom).
	
	Skok u dalj za jednog takmicara traje 1 sekundu. Bacanje koplja 2 sekunde.
	Metodu skaci poziva skakac u dalj. Metoda vraca duzinu u metrima koliko je takmicar skocio 
	(izmedju 0 i 9 metara moze skociti) i koliko je ukupno trebalo vremena da zavrsi skok 
	(koliko je zajedno trajalo cekanje i skakanje).
	Metodu baciKoplje poziva bacac koplja. Metoda vraca duzinu u metrima koliko je takmicar bacio koplje 
	(izmedju 0 i 100 metara moze baciti) i koliko je ukupno trebalo vremena da zavrsi bacanje koplja
	(koliko je zajedno trajalo cekanje i bacanje koplja).
*/

#include <iostream>
#include <mutex>
#include <thread>
#include <condition_variable>
#include <chrono>
#include <random>

using namespace std;
using namespace chrono;

struct povratna_vrednost {
    int duzina;
    duration<double, milli> trajanje;
};

class AtletskaStaza {
	int broj_skakaca;
	int broj_bacaca;
	bool slobodno;
	mutex m;
	condition_variable cs, cb;
    public:
		AtletskaStaza(int bs, int bb) : broj_skakaca(bs), broj_bacaca(bb), slobodno(true) {}
		povratna_vrednost skaci() {
			auto poceo = steady_clock::now();
			unique_lock<mutex> l(m);
			while (!slobodno) {
				cs.wait(l);
			}		
			broj_skakaca--;
			slobodno = false;
			l.unlock();
			this_thread::sleep_for(seconds(2));
			auto zavrsio = steady_clock::now();
			l.lock();		
			slobodno = true;
			if (broj_bacaca > 0) {
				cb.notify_one();
			}	
			else {
				cs.notify_one();			
			}
			return povratna_vrednost{rand()%10, zavrsio - poceo};
		}
		povratna_vrednost baciKoplje() {
			auto poceo = steady_clock::now();
			unique_lock<mutex> l(m);
			while (!slobodno) {
				cb.wait(l);
			}	
			broj_bacaca--;
			slobodno = false;
			l.unlock();
			this_thread::sleep_for(seconds(2));
			auto zavrsio = steady_clock::now();
			l.lock();	
			slobodno = true;
			if (broj_skakaca > 0) {			
				cs.notify_one();
			}	
			else {
				cb.notify_one();			
			}
			return povratna_vrednost{rand()%100, zavrsio - poceo};
		}
};

void skakac(AtletskaStaza& staza, int rbr) {
	povratna_vrednost rez = staza.skaci();
	cout << "Takmicar sa brojem " << rbr 
	<< " skocio " << rez.duzina << " metara."
    << ", a cekao " << rez.trajanje.count() << " milisekundi. " << endl;
}

void bacac(AtletskaStaza& staza, int rbr) {
	povratna_vrednost rez = staza.baciKoplje();
	cout << "Takmicar sa brojem " << rbr 
	<< " bacio koplje " << rez.duzina << " metara."
    << ", a cekao " << rez.trajanje.count() << " milisekundi. " << endl;
}

int main() {
	int BROJ_SKAKACA = 7;
	int BROJ_BACACA = 5;
	AtletskaStaza as(BROJ_SKAKACA, BROJ_BACACA);
	thread t[BROJ_SKAKACA+BROJ_BACACA];
	for (int i = 0; i != BROJ_SKAKACA; i++) {
		t[i] = thread(skakac, ref(as), i);
	}
	for (int i = 0; i != BROJ_BACACA; i++) {
		t[i+BROJ_SKAKACA] = thread(bacac, ref(as), i+BROJ_SKAKACA);
	}
	for (int i = 0; i != BROJ_SKAKACA + BROJ_BACACA; i++) {
		t[i].join();
	}
	return 0;
}
