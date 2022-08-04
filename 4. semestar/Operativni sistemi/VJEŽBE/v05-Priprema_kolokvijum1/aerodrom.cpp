/*
Modelovati koriscenje piste na aerodromu.
*/

#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <random>
#include <vector>

using namespace std;
using namespace chrono;

mutex mx;
condition_variable v;

class Aerodrom {
private:
	bool zauzeto_lijevo;
	bool zauzeto_desno;
	double relativna_l_duzina;
	double relativna_d_duzina;
	vector<int> pokusaji_sletanja;
	mutex m;
	condition_variable c;
	const int ukupno_trajanje_sletanja = 379;
	double brzina_vjetra;
public:
	int broj_aviona;
	steady_clock::time_point last_change;
	Aerodrom(int ba) : broj_aviona(ba) {
		zauzeto_lijevo = false;
		zauzeto_desno = false;
		relativna_l_duzina = 0;
		relativna_d_duzina = 0;
		pokusaji_sletanja.resize(broj_aviona);
		fill(pokusaji_sletanja.begin(), pokusaji_sletanja.end(), 0);
		brzina_vjetra = 10 + (rand()%225)/15;
	} 
	string sleti(double relativna_duzina, int id) {
		
		unique_lock<mutex> l(m);
		if (!da_vjetar()) {
			pokusaji_sletanja[id] += 1;
		}
		if (pokusaji_sletanja[id] == 3) {
			broj_aviona--;
			return "odustao";
		}		
		// cout << moze_lijevo(relativna_duzina) << endl << moze_desno(relativna_duzina) << endl;
		while (!moze_lijevo(relativna_duzina, id) && !moze_desno(relativna_duzina, id)) c.wait(l); 
		string retVal;
		if (moze_lijevo(relativna_duzina, id)) {
			zauzeto_lijevo = true;
			relativna_l_duzina = relativna_duzina;
			cout << "Pocelo sletanje " << id << endl;
			l.unlock();
			this_thread::sleep_for(seconds((int)((relativna_duzina * ukupno_trajanje_sletanja)/10000)));			
			l.lock();	
			zauzeto_lijevo = false;
			relativna_l_duzina = 0;
			retVal = "lijevo";
		}
		else if (moze_desno(relativna_duzina, id)) {
			zauzeto_desno = true;
			relativna_d_duzina = relativna_duzina;
			l.unlock();
			this_thread::sleep_for(seconds((int)((relativna_duzina * ukupno_trajanje_sletanja)/10000)));
			l.lock();	
			zauzeto_desno = false;
			relativna_d_duzina = 0;
			retVal = "desno";
		}	
		//if (moze_desno(relativna_duzina) || moze_lijevo(relativna_duzina)) {
			c.notify_all();
		// } 
		broj_aviona--;
		return retVal;
	}
	bool moze_lijevo(double relativna_duzina, int id) {
		return da_vjetar() && !zauzeto_lijevo && (!zauzeto_desno || (relativna_d_duzina + relativna_duzina < 100));
	}
	bool moze_desno(double relativna_duzina, int id) {
		return da_vjetar() && !zauzeto_desno && (!zauzeto_lijevo || (relativna_l_duzina + relativna_duzina < 100));
	}
	bool da_vjetar() {
		return brzina_vjetra < 20.39;	
	}
	void promjeni_vjetar() {
		brzina_vjetra = 10 + (rand()%225)/15 ;
		last_change = steady_clock::now();
		cout << "Brzina vjetra: " << brzina_vjetra << endl;
	}
};

void avion(Aerodrom& a, int id_aviona, double relativna_duzina) {
	string strana = a.sleti(relativna_duzina, id_aviona);
	if (strana == "odustao") {
		cout << "Avion broj " << id_aviona << " je odustao." << endl;
	}
	else {
		cout << "Sletio	avion broj " << id_aviona << " duzine " << relativna_duzina <<  " " << strana << endl;
	}
}

void vjetar(Aerodrom& a) {
	unique_lock<mutex> l(mx);
	while (true) {
		cout << a.broj_aviona << endl;
		if (steady_clock::now() - a.last_change < seconds(1)) {
			l.unlock();
			this_thread::sleep_for(seconds(1));
			l.lock();
		}
		a.promjeni_vjetar();
		
	}
}

int main() {
	int BROJ_AVIONA = 20;
	Aerodrom a(BROJ_AVIONA);
	thread t[BROJ_AVIONA];
	for (int i = 0; i != BROJ_AVIONA; i++) {
		t[i] = thread(avion, ref(a), i, 10+(rand()%10)*10);
	}
	thread v(vjetar, ref(a));
	for (int i = 0; i != BROJ_AVIONA; i++) {
		t[i].join();
	} 
	v.detach();
	return 0;
}











