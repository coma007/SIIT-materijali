/*
Modelovati placanje robe u trznom centru. U trznom centru postoje 2 kase za placanje.
Kupac pri placanju staje u red na onu kasu na kojoj ceka manji broj kupaca.
Kupac vrsi placanje pozivom metode kupi() koja kao parametar dobija broj artikala koje kupac placa.
Placanje robe traje onoliko sekundi koliko ima artikala.
Povratna vrednost metode je identifikator kase na kojoj je placanje izvrseno.
*/

#include <thread>
#include <iostream>
#include <mutex>
#include <condition_variable>

using namespace std;

class Prodavnica {
    private:
        mutex m;                                // propusnica za sprecavanje stetnog preplitanja pri pristupu atributima klase
        bool kasa_slobodna[2];                  // da li su kase slobodne - prvi element niza se odnosi na prvu kasu, a drugi na drugu
        condition_variable redovi[2];           // uslovne promenljive koje omogucuju zaustavljanje niti u cekanju na kasi - 2 promenljive za 2 kase
        int cekaju[2];                          // broj ljudi koji cekaju u redovima na kasama - prvi element niza se odnosi na ljude na prvoj kasi, a drugi na drugoj
    public:
        Prodavnica() {
            kasa_slobodna[0] = true;            // inicijalno su obe kase slobodne
            kasa_slobodna[1] = true;
            cekaju[0]  = 0;                     // inicijalno na obe kase niko ne ceka
            cekaju[1]  = 0;
        }
        int kupi(int broj_artikala) {           // metoda kao parametar prima broj artikala koje kupac kupuje
            unique_lock<mutex> l(m);
            int moja_kasa;                      // kasa na kojoj kupac kupuje ili staje u red, ako ima ispred  njega drugih kupaca
            if (cekaju[0] < cekaju[1])          // kupac bira da stane na kasu na kojoj manje ljudi ceka
                moja_kasa = 0;
            else
                moja_kasa = 1;

            cekaju[moja_kasa]++;                // staje u red, sada je jedan vise koji ceka na toj kasi
            while (!kasa_slobodna[moja_kasa])   // dok god kasa u kojoj je stao u red nije slobodna, mora da saceka
                    redovi[moja_kasa].wait(l);

            kasa_slobodna[moja_kasa] = false;   // kasa se oslobodila, ne mora vise da ceka, staje na kasu i zauzima je
            l.unlock();                         // dok nit odlazi u spavanje, ne treba drugima onemogucavati da rade sa atributima ove klase, zato otkljucamo propusnicu
            this_thread::sleep_for(chrono::seconds(broj_artikala)); //simuliranje trajanje kupovine - traje onoliko sekundi koliko ima proizvoda
            l.lock();                           // ponovo je potreban pristup deljenim promenljivima, pa se mora zatraziti propusnica pre nego se pristupi ovim promenljivim
            cekaju[moja_kasa]--;                // zavrsio je kupovinu, ne ceka vise u redu
            kasa_slobodna[moja_kasa] = true;    // oslobadja kasu
            redovi[moja_kasa].notify_one();     // javlja narednom kupcu koji ceka u redu
            return moja_kasa+1;                 // rezultat metode je broj kase na kojoj je kupovina izvrsena (posto indeksi u nizu idu od 0, dodaje se 1 da bi korisnik dobio rezultat 1 ili 2)
        }
};

mutex term_m;                                   // propusnica za sprecavanje stetnog preplitanja kod pristupa terminalu prilikom ispisa
void kupac(Prodavnica &p, int kolicina) {
    thread::id i = this_thread::get_id();       // identifikator niti - zbog razlikovanja niti pri ispisu
    {
        unique_lock<mutex> l(term_m);
        cout << "Kupac " << i << " zeli da kupi "
             << kolicina << " komada robe." << endl;
    }
    int kasa = p.kupi(kolicina);                // kupac ide u prodavnicu i vrsi kupovinu prosledjene kolicine robe (posle moguceg cekanja zbog guzve na kasi)
    {
        unique_lock<mutex> l(term_m);
        cout << "Kupac " << i << " kupio na kasi " << kasa
             << ", " << kolicina << " komada robe." << endl;
    }
}

const int KUPACA = 10;
int main() {
    Prodavnica p;
    thread t[KUPACA];
    for (int i = 0; i < KUPACA; ++i)
        t[i] = thread(kupac, ref(p), i+1);

    for (int i = 0; i < KUPACA; ++i)
        t[i].join();
}
