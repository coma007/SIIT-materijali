/*
Modelovati napadacku akciju fudbalskog kluba Barselona.
Tim sadrzi 11 igraca. Ponasanje igraca predstavljeno je datom funkcijom igrac.
Igraci medjusobno dodaju loptu, koja je predstavljena datom klasom Lopta.

Igrac mora da saceka da dobije loptu. Kada dobije loptu, igrac drzi loptu slucajan
vremenski period izmedju 1 i 3 sekunde i predaje je bilo kojem drugom igracu.
Pri predaji, lopta moze da ide unapred
(prema protivnickom golu) ili unazad. 2/3 predaja lopti ide ka napred.

Nakon 12 predaja lopti unapred, Barselona postize gol, cime se program zavrsava.
Ako pri predaji lopte igrac postigne gol, metoda dodaj_loptu vraca broj dresa igraca koji je postigao gol.
Nakon postignut gola, za sve ostale igrace metoda dodaj_loptu treba da vrati vrednost 0.
Ako gol nije postignut, metoda vraca vrednost "-1".

Barselona nikad ne gubi loptu.
*/

#include <thread>
#include <iostream>
#include <mutex>
#include <condition_variable>

using namespace std;
using namespace chrono;

class Lopta {
private:
    mutex m;
    int potrebno_za_gol;                                    // Broj potrebnih dodavanja napred da bi se postigao gol
    int broj_dodavanja;                                     // Trenutni brojac dodavanja
    bool lopta_slobodna;                                    // Indikator da li neki igrac vec drzi loptu u posedu    
    condition_variable red_za_loptu;                        // Red u koji se uvezuju igraci koji zele da prime loptu
    bool pao_gol;                                           // Indikator da je go dat. Kada postane 1 niti prestaju rad.
public:
    Lopta(int n): potrebno_za_gol(n), broj_dodavanja(0), lopta_slobodna(true), pao_gol(false) {}
    int dodaj_loptu(int broj_dresa) {
        unique_lock<mutex> l(m);
        while (!lopta_slobodna && !pao_gol)                 // Dok god je lopta zauzeta i nije pao gol cekaj. Kada lopta postane slobodna
            red_za_loptu.wait(l);                           // ili padne gol ovaj uslov postaje false. Obratiti paznju na logiku.

        if (pao_gol)                                        // Ukoliko je vec pao gol, nit prekida rad.
            return 0;

        lopta_slobodna =  false;                            // Ukoliko nije pao gol, igrac zauzima loptu.
        l.unlock();
        this_thread::sleep_for(seconds(rand() % 3 + 1));    // Drzi je u posedu do 3 sekunde.
        l.lock();
        bool napred = rand() % 3 == 2 ? false : true;       // Odredjuje da li ce dodati napred ili nazad.

        if (napred)                                         // Ako dodaje napred, povecava se broj dodavanja koji vodi ka golu.
            broj_dodavanja++;

        lopta_slobodna = true;                              // Lopta se oslobadja tj. moze da je preuzme drugi igrac
        if (broj_dodavanja == potrebno_za_gol) {            // Ako je doslo do zadnjeg dodavanja potrebnog za gol
            pao_gol = true;                                 // Postavi da je dat gol.
            red_za_loptu.notify_all();                      // Notificiraj sve ostale igrace (da ne bi cekali loptu vise).
            return broj_dresa;                              // Vrati broj dresa igraca koji je dao gol.
        }
        else {
            red_za_loptu.notify_one();                      // U suprotnom ako je dodavanje obicno, javi samo sledecem igracu koji ceka
            return -1;                                      // da moze da preuzme loptu.
        }
    }
};

mutex term_m;
void igrac(Lopta &lopta, int broj_dresa) {
    {
        unique_lock<mutex> l(term_m);
        cout << "Igrac sa brojem " << broj_dresa << " je izasao na teren." << endl;
    }
    int strelac = -1;
    do {                                                    // Dodavanje se vrsi ciklicno, tj. igrac doda. pa ponovo udje u red za 
                                                            // cekanje dodavanja. Ovo je i realan scenario jer se moze desiti da 
                                                            // isti igrac napravi vise dodavanja.
        strelac = lopta.dodaj_loptu(broj_dresa);
        cout << "Igrac " << broj_dresa << " dodao loptu." << endl;
        this_thread::sleep_for(seconds(1));                 // Igrac trci 1 seknudu izmedju cekanja za novi posed lopte.
        if (strelac > 0) {                                  // Ako je gol postignut ispise se na ekran.
            unique_lock<mutex> l(term_m);
            cout << "GOOOOL!!! Pogodak je postigao igrac sa brojem " << strelac << "!" << endl;
        }
    } while (strelac == -1);
}

const int IGRACA = 11;

int main() {
    Lopta l(12);
    thread igraci[IGRACA];
    for (int i = 0; i < IGRACA; ++i)
        igraci[i] = thread(igrac, ref(l), i+1);

    for (int i = 0; i < IGRACA; ++i)
        igraci[i].join();
}


