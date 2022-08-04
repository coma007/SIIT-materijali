// Napisati konkurentni program koji modeluje pivnicu.
// U pivnici postoji ogranicen broj mesta (konstanta STOLICA_U_PIVNICI).

// Pivopija poziva operaciju udji() kada zeli da udje u pivnicu.
// Pivopija ulazi u pivnicu ako u pivnici ima mesta, inace ceka da se 
// pojavi slobodno mesto.

// Kada udje u pivnicu, pivopija narucuje pivo pozivanjem operacije naruci().
// Tocenje velikog piva traje 2 sekunde, a malog 1 sekundu.
// Tokom tocenja barmen je zauzet i ne moze da opsluzuje druge pivopije.

// Kada dobije pivo pivopija provede jos neko vreme u pivnici pijuci ga,
// a zatim napusti pivnicu pozivom operacije izadji().

// Stvoriti 10 pivopija (5 piju malo, a 5 veliko pivo)

// Komentari su obavezni.


#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

class Pivnica {
    mutex m_ulazIzlaz;                      // propusnica za pristup deljenim resursima u klasi
    mutex m_barmen;                         // propusnica za iskljucivi region za pristup barmenu
    condition_variable slobodna_stolica;    // red cekanja na slobodnu stolicu
    condition_variable barmen;              // red cekanja na barmena da natoci pivo
    int slobodnih_stolica;                  // trenutni broj slobodnih stolica
public:
    enum Pivo { VELIKO, MALO };                             // dva moguca tipa piva
    Pivnica(int stolica) : slobodnih_stolica(stolica) {}    // inicijalno su sve stolice slobodne
    void udji() {
        unique_lock<mutex> lock(m_ulazIzlaz);               // zakljucavanje propusnice pre pristupa deljenom resursu "slobodnih_stolica"
        while(slobodnih_stolica==0) {                       // dok god nema nijedna slobodna stolica, musterija ceka
            slobodna_stolica.wait(lock);
        }
        --slobodnih_stolica;                                // kada je izasao iz cekanja, znaci da se oslobodila jedna stolica, koju klijent zauzima. Dakle, jedna slobodna stolica manje
    }
    void izadji() {
        unique_lock<mutex> lock(m_ulazIzlaz);               // zakljucavanje propusnice pre pristupa deljenom resursu "slobodnih_stolica"
        ++slobodnih_stolica;                                // musterija napusta pivnicu. Dakle, jedna slobodna stolica vise
        slobodna_stolica.notify_one();                      // javljamo jednom od onih koji cekaju da udju u pivnicu da sad ima jedna slobodna stolica
    }
    void naruci(Pivo velicina_piva) {
                                                            // Za barmena nije neophodna condition_variabla jer se 
                                                            // serijalizacija opsluzivanja dogadja na mutex-u.
        unique_lock<mutex> lock(m_barmen);                  // zakljucavanjem propusnice obezbedili smo pristup barmenu po principu jedna-po-jedna musterija
        if(velicina_piva == VELIKO)                         // simuliranje trajanja tocenja. tocenje traje srazmerno tipu piva
            this_thread::sleep_for(chrono::seconds(2));
        else
            this_thread::sleep_for(chrono::seconds(1));
    }
};

void pivopija(Pivnica& pivnica, Pivnica::Pivo velicina_piva) {
    static mutex term_m;
    {
        unique_lock<mutex> l(term_m);
        cout  << this_thread::get_id() << " Pokusavam da udjem u pivnicu..." << endl;
    }
    pivnica.udji();
    {
        unique_lock<mutex> l(term_m);
        cout  << this_thread::get_id() << " Usao u pivnicu. Narucujem";
        if(velicina_piva == Pivnica::VELIKO)
            cout << " VELIKO ";
        else
            cout << " MALO ";
        cout << "pivo." << endl;
    }
    pivnica.naruci(velicina_piva);
    // 3 sekunde pivopija pije pivo, a zatim napusta pivnicu.
    this_thread::sleep_for(chrono::seconds(3));
    {
        unique_lock<mutex> l(term_m);
        cout  << this_thread::get_id() << " Popio. Odoh..." << endl;
    }
    pivnica.izadji();
};

const int PIVOPIJA = 10;
const int STOLICA_U_PIVNICI = 3;
int main() {
   Pivnica pivnica{STOLICA_U_PIVNICI};
   thread t[PIVOPIJA];
   for(int i = 0; i < PIVOPIJA; ++i)
      t[i] = thread(pivopija, ref(pivnica), (Pivnica::Pivo)(i % 2)); //parni narucuju malo pivo, a neparni veliko
   for(int i = 0; i < PIVOPIJA; ++i)
      t[i].join();
}
