// Modelovati salter salu u posti u kojoj postoje 2 saltera.

// Vremensko trajanje uplate (boravak klijenta na salteru) je srazmerno 
// velicini uplate. Za svaku uplacenu hiljadu dinara klijent ceka 1 sec.
// Na salteru se moze uplatiti maksimalno 4 hiljada dinara.
// (podrazumeva se da je ispravna vrednost prosledjena klijentu 
// pri stvaranju niti).

// Kada klijent zeli da uplati sredstava, on poziva operaciju uplati(), 
// cime prakticno ulazi u postu i staje u red.
// Povratna vrednost ove operacije je broj saltera na kojem je klijent
// izvrsio uplatu i svota koja je do tog trenutka na salteru uplacena.

// Treba stvoriti 7 klijenata.


#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

struct povratna_vrednost {                              // povratna vrednost funkcije "uplati". Cuva podatke o tome koji je salter u pitanju i koliko je do tog trenutka na njemu uplaceno
    int salter;
    int uplaceno;
    povratna_vrednost(int s, int u) : salter{s}, uplaceno{u} {}
};

class posta {
    int uplaceno[2];                                    // prvi element niza se odnosi na kolicinu novca uplacenu na prvom salteru, a drugi element na drugom
    condition_variable red;                             // uslovna promenljiva za uvezivanje niti u red cekanja na uslov
    bool salter_zauzet[2];                              // prvi element niza se odnosi na to da li je prvi salter zauzet, a drugi element da li je drugi zauzet
    mutex m;                                            // propusnica za iskljucivi region pri pristupu deljenim resursima
public:
    posta() {                                           // inicijalno su oba saltera slobodna i nista na njima nije uplaceno
        uplaceno[0]=0; uplaceno[1]=0; 
        salter_zauzet[0]=false; salter_zauzet[1]=false; 
    }

    povratna_vrednost uplati(int svota) {               // parametar je svota koju klijent uplacuje
        unique_lock<mutex> l(m);                        // zakljucavanje propusnice zbog pristupa deljenim resursima
        while(salter_zauzet[0] && salter_zauzet[1])     // dok god su oba saltera zauzeta, klijent mora da saceka
            red.wait(l);
                                                        // jedan salter se oslobodio. Naredna linija utvrdjuje koji je to salter i upamti redni broj saltera u promenljivu "salter".
        int salter = salter_zauzet[0] ? 1 : 0; 
        salter_zauzet[salter] = true;                   // klijent zauzima salter koji se oslobodio
        l.unlock();                                     // placanje ce da potraje. Za to vreme treba pustiti druge klijente da rade svoj posao, nema razloga da drzimo propusnicu
        this_thread::sleep_for(chrono::seconds(svota)); // simuliranje trajanja placanja. Placanje traje broj sekundi proporcionalan svoti koja se uplacuje
        l.lock();                                       // ponovo trazimo propusnicu jer cemo pristupati deljenim resursima
        uplaceno[salter]+=svota;                        // sada je na ovom salteru ukupna uplacena kolicina novca povecana za sumu koju je klijent upravo uplatio
        salter_zauzet[salter] = false;                  // klijent oslobadja salter na kojem je izvrsio uplatu
        red.notify_one();                               // javlja nekom od onih koji cekaju da se jedan salter oslobodio
        return povratna_vrednost{salter,uplaceno[salter]}; // rezultat metode je promenljiva koja sadrzi podatak gde je uplaceno i koliko ukupno do sada
    }
};

void klijent(posta& p, int svota) {
   static mutex term_m;
   {
      unique_lock<mutex> l(term_m);
      cout << "Klijent broj: " << this_thread::get_id() 
           << " zeli da uplati " << svota
           << " hiljada dinara." << endl;
   }
   auto ret = p.uplati(svota);
   {
      unique_lock<mutex> l(term_m);
      cout << "Klijent broj: " << this_thread::get_id() << " ("
           << svota << ") salter " << ret.salter 
           << " (" << ret.uplaceno << ")"<< endl;
   }
}

constexpr int KLIJENATA = 7;
int main() {
   posta p; 
   thread t[KLIJENATA];
   for(int i = 0; i < KLIJENATA; ++i)
      t[i] = thread(klijent, ref(p), i * 3 % 4 + 1);    // za svotu se prosledjuje uvek razlicita vrednost, zavisno od rednog broja klijenta
   for(int i = 0; i < KLIJENATA; ++i)
      t[i].join();
}
