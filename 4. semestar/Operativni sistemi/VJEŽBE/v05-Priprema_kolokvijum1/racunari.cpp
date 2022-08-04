/*Modelovati koriscenje racunara u racunarskoj ucionici. Broj racunara u ucionici se prosledjuje pri inicijalizaciji.
Student pozivom operacije zauzmi() dolazi u ucionicu i zauzima prvi slobodan racunar, ukoliko takav racunar postoji.
Ukoliko su svi racunari zauzeti, student mora sacekati da se neki racunar oslobodi.
Operacija zauzmi() vraca redni broj racunara koji je student zauzeo.
Student koristi racunar neki slucajan broj sekundi.
Operacijom oslobodi(), student zavrsava rad u ucionici. Parametar metode je redni broj racunara koji student koristi i koji
treba da se oslobi.
*/

#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <vector>

using namespace std;

class RC {
	const int broj_racunara;
	int broj_slobodnih;
	vector<bool> zauzeti_racunari;
	mutex m;
	condition_variable cv;
	public:
		RC(int br) : broj_racunara(br), broj_slobodnih(br) {
			zauzeti_racunari.resize(br);
			fill(zauzeti_racunari.begin(), zauzeti_racunari.end(), false);	
		}
		int zauzmi() {
			unique_lock<mutex> l(m);
			while (broj_slobodnih == 0) {
				cv.wait(l);
			}
			broj_slobodnih--;
			for (int i = 0; i != broj_racunara; i++) {
				if (zauzeti_racunari[i] == false) {
					zauzeti_racunari[i] = true;
					return i;			
				}			
			}
			return -1;
		}
		void oslobodi(int id_racunara) {
			unique_lock<mutex> l(m);
			zauzeti_racunari[id_racunara] = false;
			broj_slobodnih++;
			cv.notify_one();			
			}

};

mutex term_mx;

void student(RC &rc, int br_indeksa) {
    {
        unique_lock<mutex> l(term_mx);
        cout << "Student " << br_indeksa
		<< " zeli da koristi ucionicu. " << endl;
    }
    int id_racunara  = rc.zauzmi();
    {
        unique_lock<mutex> l(term_mx);
        cout << "Student " << br_indeksa 
		<< " seo za racunar " << id_racunara << endl;
    }
    this_thread::sleep_for(chrono::seconds(rand()%5 + 1));
    rc.oslobodi(id_racunara);
    {
        unique_lock<mutex> l(term_mx);
        cout << "Student " << br_indeksa 
		<< " zavrsio rad u ucionici." << endl;
    }
}

int main() {
	RC rc(5);
	const int BROJ_STUDENATA = 10;
	thread t[BROJ_STUDENATA];
	for (int i = 0; i != BROJ_STUDENATA; i++) {
		t[i] = thread(student, ref(rc), i);
	}
	for (int i = 0; i != BROJ_STUDENATA; i++) {
		t[i].join();
	}	
	return 0;
}
