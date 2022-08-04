/*
Modelovati soping na rasprodaji.
Kupci dolaze u prodavnicu da kupe odecu.

Kupac najpre probava odecu u jednoj od kabina za probavanje.
Broj kabina za probavanje prosledjuje se pri instanciranju klase Prodavnica.
Ako su sve kabine zauzete, kupac mora da saceka sa probavanjem dok se neka kabina ne oslobodi.

Nakon probavanja odece, kupac vrsi kupovinu, ako mu odeca odgovara.
Sansa da mu odeca odgovara je 50%.
Probavanje odece traje 1 sekundu.

Metoda "kupi" vraca informaciju da li je kupac kupio odecu i koliko dugo je cekao da 
udje u kabinu.

Data funkcija "kupac" modeluje ponasanje kupca.
Ako mu isprobana odeca ne odgovara, kupac odlazi da pronadje
drugi komad odece i onda ponovo odlazi da proba odecu u kabini.
*/

#include <thread>
#include <iostream>
#include <mutex>
#include <condition_variable>

using namespace std;
using namespace chrono;

struct povratna_vrednost {
    bool kupio;
    duration<double, milli> cekao_na_kabinu;
};

class Prodavnica {
    private:
        int slobodnih_kabina;                                       // Broj slobodnih kabina
        mutex m;
        condition_variable c;
    public:
        Prodavnica(int n): slobodnih_kabina(n) {}
        povratna_vrednost kupi() {
            povratna_vrednost pv;
            unique_lock<mutex> l(m);
            system_clock::time_point dosao = system_clock::now();
            while (slobodnih_kabina == 0)                           // Ako nema slobodnih kabina, cekaj.
                c.wait(l);

            pv.cekao_na_kabinu = system_clock::now() - dosao;

            slobodnih_kabina--;
            l.unlock();
            this_thread::sleep_for(seconds(1));                     // proba odecu
            l.lock();

            pv.kupio = rand()%2;                                    // Da li je kupio ili nije. Tj. 0 ili 1.
            slobodnih_kabina++;                                     // Povecava se broj slobodnih kabina.
            c.notify_one();                                         // Obavesti sledeceg kupca da moze uci u kabinu.

            return pv;
        }
};

mutex term_m;
void kupac(Prodavnica &p, int id_kupca) {
    {
        unique_lock<mutex> l(term_m);
        cout << "Kupac " << id_kupca << " usao u prodavnicu." << endl;
    }
    povratna_vrednost pv;
    do {
        pv = p.kupi();
        unique_lock<mutex> l(term_m);
        if (pv.kupio)
            cout << "Kupac " << id_kupca << " kupio odecu. Cekao na kabinu: "
                << pv.cekao_na_kabinu.count() << " milisekundi." << endl;
        else {
            cout << "Kupac " << id_kupca << " nije kupio odecu. Cekao na kabinu: "
                << pv.cekao_na_kabinu.count() << " milisekundi." << endl;
            this_thread::sleep_for(seconds(1));                     // kupac trazi novi komad odece
        }
    } while (!pv.kupio);                                            // Radi probu sve dok ne uspes da pronadjes odgovarajucu odecu.
}

const int KUPACA = 10;
int main() {
    Prodavnica p(3);
    thread kupci[KUPACA];
    for (int i = 0; i < KUPACA; ++i)
        kupci[i] = thread(kupac, ref(p), i+1);

    for (int i = 0; i < KUPACA; ++i)
        kupci[i].join();
}
