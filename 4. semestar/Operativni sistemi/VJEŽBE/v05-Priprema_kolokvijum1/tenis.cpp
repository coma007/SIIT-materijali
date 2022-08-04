/*
Modelovati prvo kolo teniskog turnira koje se odrzava u teniskom klubu sa n terena.
Svaki teren ima svoj broj. (Brojevi su od 1 do 12).

Na terenima se igraju teniski mecevi prvog kola teniskog turnira. U prvom kolu ucestvuje X takmicara, 
tako da ima M = X/2 teniska meca. Za svaki mec u startu se definise na kojem terenu ce biti odigran. 
Raspored meceva po terenima pravi se tako da se mecevi ravnomerno rasporede po terenima. Znaci, na svakom terenu 
se u proseku igraju n/M meca. Svaki mec ima svoj identifikator (broj).

Svaki mec traje slucajan vremenski period izmedju 1 i 5 sekundi. Naredni mec na terenu ne moze da pocne dok 
se prethodni mec na tom terenu ne zavrsi.

Za svaki mec potrebno je evidentirati trenutak kada je mec poceo i koliko je mec trajao.

 Napomene:
    Komentari su obavezni.    
	Za dobijanje slucajnog broja koristiti datu funkciju rand_sync
*/

#include <thread>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <mutex>
#include <condition_variable>

#define MAX_TERENA 30

using namespace std;
using namespace chrono;

int rand_sync() {                               // Thread safe random. Da ne bi razlicite niti dobile iste random brojeve.
        static mutex mx;
        unique_lock<mutex> l(mx);
        return rand();
}

struct podaci {                                 // Podaci o mecu. Broj meca, trajanje i trenuci dolaska i pocetka.
    int brojMeca;
    duration<double, milli> trajanje;
    steady_clock::time_point dosao;
    steady_clock::time_point pocetak;
};

class TeniskiKlub {                             // Klasa deljenog resursa. Pravi se maksimalno 30 terena, ali ce u realnosti
    private:                                    // biti samo 3 terena.
        mutex mx;
        condition_variable uslovi[MAX_TERENA];  // Svaki teren ima svoju CV na kojoj igraci moraju cekati ako je teren zauzet.
        bool slobodni[MAX_TERENA];              // Svaki teren je ili slobodan ili zauzet, od cega zavisi i cekanje.
    public:
        TeniskiKlub(int ukupnoTerena);
        podaci odigrajMec(int, int);
};

mutex term_mx;

void mec(TeniskiKlub& tk, int brojMeca, int naTerenu) {     // Nit meca. Prosledjuje se broj meca i na kom terenu se igra.
    podaci v = tk.odigrajMec(brojMeca, naTerenu);

    duration<double, milli> cekao = v.pocetak - v.dosao;
    unique_lock<mutex> l(term_mx);
    cout << "Mec " << v.brojMeca + 1 << " odigran na terenu " << naTerenu + 1 << " trajao " << v.trajanje.count() << " milisekundi. Takmicari su na pocetak meca cekali " << cekao.count()
        << " milisekundi. " << endl;
}

TeniskiKlub::TeniskiKlub(int ukupnoTerena) {                // Konstruktor. Na pocetku su svi tereni slobodni.
    for (int i = 0; i < ukupnoTerena; ++i) {
        slobodni[i]= true;
    }
}

podaci TeniskiKlub::odigrajMec(int brojMeca, int naTerenu) { // Funkcija koju zove nit mec. 
    podaci p;
    p.brojMeca = brojMeca;                                  // U podatke se belezi broj meca kao i vremena dolaska, pocetka i trajanja.
    {
        p.dosao = steady_clock::now();                      // Belezenje vremena moze van kriticne sekcije (nije deljeni resurs).
        unique_lock<mutex> lock(mx);
        while (!slobodni[naTerenu]) {                       // Dogod je zauzet teren na kojem hocemo da igramo cekamo da se oslobodi.
            uslovi[naTerenu].wait(lock);
        }
        p.pocetak = steady_clock::now();
        slobodni[naTerenu] = false;                         // Zauzimamo teren.
    }
    this_thread::sleep_for(seconds(rand_sync()%5 + 1));     // Mec se igra do 5 sekundi. Za to vreme propusnica se oslobadja.
    p.trajanje = steady_clock::now() - p.pocetak;

    unique_lock<mutex> lock(mx);
    slobodni[naTerenu] = true;                              // Teren se oslobadja.
    uslovi[naTerenu].notify_one();                          // Notificra se sledeci mec koji ceka na taj teren.

    return p;
}

int main() {
    int ukupnoTerena = 3;
    TeniskiKlub tk(ukupnoTerena);
    int brojTakmicara = 20;
    int brojMeceva = brojTakmicara/2;                      // Logicno, meceva ima polovina od broja takmicara.

    thread mecevi[brojMeceva];

    for (int i = 0; i < brojMeceva; ++i) {                 // Svi mecevi se ciklicno rasporedjuju na terene 1, 2 i 3.
        mecevi[i] = thread(mec, ref(tk), i, i%ukupnoTerena);
    }

    for (int i = 0; i < brojMeceva; ++i) {
        mecevi[i].join();
    }

    return 0;
}

