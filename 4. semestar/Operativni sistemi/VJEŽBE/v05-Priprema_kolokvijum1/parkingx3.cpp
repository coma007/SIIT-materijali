// Parking sa 3 ulaza i jednim mestom.
// Na parking automobili ulaze sa ulaza 0, 1 i 2 po round-robin protokolu
// (jedan udje sa prvog, jedan sa drugog, jedan sa treceg i tako u krug).

// Automobilu se pri stvaranju prosledjuje vreme (u sekundama) koje se on 
// zadrzave na parkingu.
// U programu uvek ima jednak broj automobila na svim ulazima!


#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

class parking {
    mutex m;                        // propusnica za pristup deljenim resursima u klasi
    condition_variable na_ulazu[3]; // tri reda cekanja - za svaki ulaz po jedan
    int slobodnih_mesta;            // trenutni broj slobodnih mesta na parkingu 
    int aktivan_ulaz;               // ulaz na koji treba da udje naredni automobil
public:
    parking() : slobodnih_mesta(1), aktivan_ulaz(0) {}      // posto parking ima jedno mesto koje je inicijalno slobodno. Prvo cemo dozvoliti ulaz sa prvog ulaza
    void udji(int ulaz) {                                   // parametar je ulaz na koji se automobil pojavljuje
        unique_lock<mutex> l(m);                            // zakljucavamo propusnicu pre pristupa deljenim resursima u klasi
        while(slobodnih_mesta==0 || aktivan_ulaz!=ulaz) {   // dok god je parking zauzet ili se naredni automobil pusta sa nekog drugog ulaza, automobil mora da ceka
            na_ulazu[ulaz].wait(l);                         // uvezivanje u red cekanja na ulazu na koji je automobil dosao
        }
        --slobodnih_mesta;                                  // kada udje na parking, parking je zauzet
        aktivan_ulaz=(aktivan_ulaz+1)%3;                    // odredjivanje narednog ulaza na koji treba automobil da udje (ide se u krug 0-1-2-0-1-2-0 itd)
    }

    void izadji() { 
        unique_lock<mutex> l(m);                            // zakljucavamo propusnicu pre pristupa deljenim resursima u klasi
        ++slobodnih_mesta;                                  // pri napustanju parkinga, mesto se oslobadja
        na_ulazu[aktivan_ulaz].notify_one();                // javimo jednom automobilu u redu iz kojeg pustamo naredni automobil da moze da udje
    }
};

mutex term_m;
void automobil(parking& p, int ulaz, int ostajem_na_parkingu) {
    thread::id id = this_thread::get_id();
    {
        unique_lock<mutex> l(term_m);
        cout << "Automobil " << id << " pokusava da udje na parking na ulaz " << ulaz << endl;
    }
    p.udji(ulaz);
    {
        unique_lock<mutex> l(term_m);
        cout << "Automobil " << id << " usao na parking na ulaz " << ulaz << endl;
    }
    this_thread::sleep_for(chrono::seconds(ostajem_na_parkingu));
    p.izadji();
    unique_lock<mutex> l(term_m);
    cout << "Automobil " << id << " izasao sa parkinga." << endl;
}

const int AUTOMOBILA = 12;
int main() {
    parking p;
    thread t[AUTOMOBILA];
    for(int i = 0; i < AUTOMOBILA; ++i)
        t[i] = thread(automobil, ref(p), i%3, i%2);   // ulaz na koji automobil ide i broj sekundi koliko se zadrzava zavise od rednog broja automobila. Bitno je da dobijemo na svakom ulazu jednak broj automobila
    for(int i = 0; i < AUTOMOBILA; ++i)
        t[i].join();
}
