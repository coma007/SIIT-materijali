/*
Napraviti konkurentni program koji simulira bezbednosne
propuste pri nadzoru zatvora.

Zatvorski krug podeljen je u 8 sektora.
Na sredini zatvorskog kruga je stub na kojem je postavljena kamera.
Kamera u jednom trenutku nadzire samo jedan sektor.
Dve sekunde nadzire jedan sektor i nakon toga se pomera na
naredni sektor (pomera se kruzno uvek u istu stranu,
u smeru kazaljke na satu).
Rad kamere predstavljen je koriscenjem niti koja izvrsava
datu funkciju "kamera".

10 zatvorenika pokusava da pobegne iz zatvora.
Njihova spavaonica se nalazi u sektoru 0, koji kamera
inicijalno nadgleda. Kako se kamera pomera,
zatvorenici se krecu za njom, u istom smeru, tako da su
uvek u sektoru koji kamera ne nadgleda.
Zatvoreniku treba jedna sekunda da pretrci iz jednog sektora u
drugi.

Izlaz iz zatvora je u sektoru 4.

Zatvorenici su predstavljeni nitima koji izvrsavaju funkciju
zatvorenik.

Pomoc: Nad niti koja izvrsava funkciju "kamera",
pozvati operaciju "detach" umesto "join",
jer ova nit stalno radi i ne treba cekati da se zavrsi.

*/

#define BROJ_SEKTORA 8

#include <thread>
#include <iostream>

using namespace std;

class Zatvor {
    int nadgledani_sektor;
    int izlazni_sektor;
    mutex m;
    condition_variable sektor[BROJ_SEKTORA];
    public:
        Zatvor():
            nadgledani_sektor(0),
            izlazni_sektor(4) {}
        void pretrci(int ulaz, int br) {
            int zeljeni_sektor = ulaz;
            unique_lock<mutex> l(m);
            //ako zelimo u jedan nakon izlaznog, znaci da smo vec dosli do izlaza
            while (true) {
                while (zeljeni_sektor == nadgledani_sektor) {
                    sektor[zeljeni_sektor].wait(l);
                }

                l.unlock();
                this_thread::sleep_for(chrono::seconds(1));
                l.lock();
                cout << "Zatvorenik " << br << " pretrcao u sektor "
                    << zeljeni_sektor << endl;
                if (zeljeni_sektor == izlazni_sektor)
                        break;

                zeljeni_sektor = (zeljeni_sektor+1)%BROJ_SEKTORA;

            }
        }
        void nadgledaj() {
            while (true) {
                this_thread::sleep_for(chrono::seconds(2));
                unique_lock<mutex> l(m);
                sektor[nadgledani_sektor].notify_all();
                nadgledani_sektor=(nadgledani_sektor+1)%BROJ_SEKTORA;
                cout << "Kamera se pomerila na sektor " << nadgledani_sektor << endl;

            }
        }
};

mutex term_m;

void zatvorenik(Zatvor& z, int sektor_spavaonice, int br) {
    {
        unique_lock<mutex> l(term_m);
        cout << "Zatvorenik " << br << " pokusava da pobegne "
            << " iz spavaonice u sektoru " << sektor_spavaonice << endl;
    }
    z.pretrci(sektor_spavaonice, br);
    {
        unique_lock<mutex> l(term_m);
        cout << "Zatvorenik " << br << " pobegao. " << endl;
    }
}

void kamera(Zatvor& z) {
    z.nadgledaj();
}

const int BROJ_ZATVORENIKA = 10;

int main() {
    Zatvor z;
    thread k(kamera, ref(z));
    k.detach();

    thread zatvorenici[BROJ_ZATVORENIKA];
    for (int i = 0; i < BROJ_ZATVORENIKA; i++)
        zatvorenici[i] = thread(zatvorenik, ref(z), 0, i+1);

    for (int i = 0; i < BROJ_ZATVORENIKA; i++)
        zatvorenici[i].join();

}