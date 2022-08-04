/* 
	Modelovati iznajmljivanje jedne knjige u biblioteci. Biblioteka poseduje N primeraka ove knjige.
	Ovaj parametar se prosledjuje pri inicijaliziciji biblioteke.
	Clan iznajmljuje primerak pozivom metode iznajmi().
	Ukoliko su svi primerci trenutno na citanju, clan biblioteke mora da saceka da neki primerak bude vracen u biblioteku.
	Primerak moze da bude kod clana na citanju neki slucajan vremenski period, koji nije duzi od 4 sekunde.
	Nakon citanja, clan vraca primerak u biblioteku pozivom metode vrati().
*/

#include <thread>
#include <iostream>
#include <cstdlib>
#include <mutex>
#include <condition_variable>

using namespace std;
using namespace chrono;

int rand_sync() {                                       // thread-safe funkcija koja vraca pseudoslucajan broj
    static mutex mx;
    unique_lock<mutex> l(mx);
    return rand();
}

class Biblioteka {
private:
    mutex mx;                                           // propusnica za sprecavanje stetnog preplitanja
    condition_variable c;                               // red cekanja na knjigu
    int slobodnihPrimeraka;                             // trenutni broj slobodnih primeraka knjige
public:
    Biblioteka(int br): slobodnihPrimeraka(br) {}       // inicijalno su svi primerci slobodni
    void iznajmi();
    void vrati();
};

void Biblioteka::iznajmi() {
    unique_lock<mutex> l(mx);                           // zakljucavanje propusnice pre pristupa deljenim resursima
    while (slobodnihPrimeraka == 0) {                   // dok god nijedan primerak nije slobodan, treba da saceka
        c.wait(l);
    }
    slobodnihPrimeraka--;                               // uzima knjigu, jedan primerak manje
}

void Biblioteka::vrati() {
    unique_lock<mutex> l(mx);
    slobodnihPrimeraka++;                               // vraca knjigu, jedan primerak vise u biblioteci
    c.notify_one();                                     // javlja nekom od onih koji cekaju na knjigu da se pojavio u biblioteci slobodan primerak
}

mutex term_mx;

void clan(Biblioteka& b, int brClanskeKarte) {
    {
        unique_lock<mutex> l(term_mx);
        cout << "Clan " << brClanskeKarte << " zeli da iznajmi knjigu." << endl;
    }
    b.iznajmi();
    {
        unique_lock<mutex> l(term_mx);
        cout << "Clan " << brClanskeKarte << " iznajmio knjigu." << endl;
    }
    this_thread::sleep_for(seconds(rand_sync() % 4 + 1));
    b.vrati();
    unique_lock<mutex> l(term_mx);
    cout << "Clan " << brClanskeKarte << " vratio knjigu." << endl;
}

int main() {
    int brojPrimeraka = 3;
    int brojClanova = 10;

    Biblioteka b(brojPrimeraka);
    thread clanovi[brojClanova];

    for (int i = 0; i < brojClanova; ++i) {
        clanovi[i] = thread(clan, ref(b), i+1);
    }

    for (int i = 0; i < brojClanova; ++i) {
        clanovi[i].join();
    }

    return 0;
}