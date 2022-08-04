/*
Napraviti konkurentni program koji simulira turnir u streljastvu.

Svaki takmicar prvo poziva operaciju pucaj da bi dobio priliku da 
ispuca svojih 10 metaka.
Gadja se kruzna streljacka meta i za svaki metak moze da se osvoji
do 10 poena (kaze se i 'krugova').
Takmicenje se odvija u streljani sa samo jednom trakom, tako da u svakom
trenutku najvise jedan takmicar moze da puca.
Operacija pucaj() vraca broj poena(krugova) koje je takmicar osvojio.

Zatim svaki takmicar poziva operaciju proglasenje_pobednika().
Povratna vrednost ove operacije je mesto koje je takmicar osvojio.

Podrazumeva se dva takmicara nikad nece osvojiti isti broj poena.
*/

#include <iostream>
#include <thread>
#include <map>
#include <unordered_map>
#include <mutex>
#include <condition_variable>

using namespace std;

class Turnir {                                          // Slicno zadatku priredba. Pogledati i taj zadatak.
    unsigned metaka;                                    // Broj metaka koje moze da ispuca takmicar. 
    unsigned takmicara;                                 // Broj takmicara.
    unsigned pucali;                                    // Koliko takmicara je zavrsilo pucanje.
    mutex m;
    condition_variable svi_pucali;                      // CV koja odredjuje kada su svi takmicari zavrsili pucanje. Moraju svi pucati pre
    map<unsigned, thread::id> pogodaka;                 // proglasenja pobednika. Mapa pogodataka, kljuc je koliko krugova je pogodjeno a 
    unordered_map<thread::id, unsigned> osvojeno_mesto; // id je id niti. osvojeno_mesto jeste nesortirana mapa, tj. za 
public:                                                 // razliku od mape pogodataka koja se sortira interno prema broju pogodaka, ova 
    Turnir(unsigned takmicara_)                         // druga mapa nema sortiranje.
        : metaka(10), takmicara(takmicara_), pucali(0) 
        {}
    unsigned pucaj() {
        unique_lock<mutex> l(m);
        unsigned krugova = 0;                           // Na pocetku je broj pogodjenih krugova 0.
        for(auto i=0u; i<metaka; ++i)                   // Dogod ima metaka pucaj.
            krugova += rand() % 11;                     // Svaki metak pogadja u krugove sa razlicitom verovatnocom (do 10).
        pogodaka[krugova] = this_thread::get_id();      // Belezi se u mapi novi element kome je kljuc broj pogodjenih krugova a 
        // Da li je upravo pucao poslednji takmicar?    // vrednost id takmicara koji je pogodio date krugove.
        if(++pucali == takmicara) { 
            unsigned mesto = 0;
                                                        // Bitno je da 'pogodaka' bude ordered map-a,
                                                        // zato sto se ona ovde koristi za sortiranje takmicara.
                                                        // Poslednji u mapi je takmicar sa najvecim brojem 
                                                        // pogodjenih krugova, tj. osvajac prvog mesta...
            for(auto i = pogodaka.crbegin(); i != pogodaka.crend(); ++i) {  // od nazad ka napred (zadnji je najbolji)
                                                        // Kljuc je thread::id, a vrednost osvojeno mesto
                osvojeno_mesto[i->second] = ++mesto;
            }
            svi_pucali.notify_all();                    // Kada su svi pucali obavesti funkciju proglasnje_pobednika. Mora notify_all
        }                                               // Posto svi takmicari pre poslednjeg udju u wait.
        return krugova;
    }
    unsigned proglasenje_pobednika() {
        unique_lock<mutex> l(m);
        // Treba sacekati da svi takmicari pucaju
        while(pucali != takmicara) {
            svi_pucali.wait(l);
        }
        return osvojeno_mesto[this_thread::get_id()];   // Svaki takmicar nalazi koje je mesto osvojio iz mape osvojenih
    }                                                   // mesta. Njegovo mesto je indeksirano kljucem koji je njegov id.
};

void takmicar(Turnir& t) {                              
    static mutex term;
    {
        unique_lock<mutex> l(term);
        cout << this_thread::get_id() << " : Idem da pucam..."  << endl;
    }
    auto krugova = t.pucaj();
    {
        unique_lock<mutex> l(term);
        cout << this_thread::get_id() << " : Pogodio sam " << krugova 
             << " krugova." << endl;
    }
    //Takmicar odmara neko vreme pre proglasenja pobednika
    this_thread::sleep_for(chrono::milliseconds(10));
    auto osvojeno_mesto = t.proglasenje_pobednika();
    {
        unique_lock<mutex> l(term);
        cout << this_thread::get_id() << " : Osvojio sam " << osvojeno_mesto
             << ". mesto." << endl;
    }
}

const unsigned TAKMICARA = 5;
int main() {
    Turnir turnir(TAKMICARA);
    thread t[TAKMICARA];
    for(auto i = 0u; i < TAKMICARA; ++i)
        t[i] = thread(takmicar, ref(turnir));
    for(auto i = 0u; i < TAKMICARA; ++i)
        t[i].join();
}
