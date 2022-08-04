/*
Modelovati pogranicni prelaz sa 4 rampe za propustanje (gledano samo u jednom pravcu) pri cemu su tri rampe za automobile, 
a jedna za kamione. 

Od toga je jedna automobilska rampa za automobile iz Evropske unije a ostale 2 za automobile iz ostalih zemalja. 
Automobili ulaze na rampe (ako postoji slobodna odgovarajuceg tipa a u suprotnom cekaju). 

Obicni automobili cekaju na jednoj od 2 rampe za obicne automobile, sa tim sto cekaju na rampi na kojoj je red cekanja kraci. 
Zadrzavaju se na rampama onoliko sekundi koliko ima putnika (maksimalno 5). 

Na rampi za kamione kamioni se zadrzavaju onoliko sekundi koliko imaju robe u sebi.

Komentari su obavezni!
*/

#include <iostream>
#include <thread>
#include <set>
#include <string>
#include <mutex>
#include <condition_variable>

using namespace std;

int rand_sync() {                               // Thread safe funkcija random. Neophodna da 2 niti ne bi dobile isti      
    static mutex mx;                            // random broj.
    unique_lock<mutex> l(mx);
    return rand();
}

enum tip_vozila { EU_AUTOMOBIL=0, OBICAN_AUTOMOBIL, KAMION };   // Enumeracija tipova vozila.


class prelaz {
   mutex m;
   condition_variable prelaz_eu;                    // Uslovne promenljive za razlicite tipove prelaza (vozila).
   condition_variable prelaz_obican[2];
   condition_variable prelaz_kamioni;
   bool prelaz_eu_zauzet;                           // Uslovi koji odredjuju da li vozila cekaju ili prolaze odredjeni prelaz.
   bool prelaz_obicni_zauzet[2];
   bool prelaz_kamioni_zauzet;
   int obicnih_automobila[2];                       // Brojac obicnih automobila na svakom od obicnih prolaza.
public:
    prelaz() {
        prelaz_eu_zauzet = false;                   // Na pocetku su svi prelazi slobodni i nema automobila.
        prelaz_kamioni_zauzet = false;
        for (int i=0;i<2;i++) {
            obicnih_automobila[i] = 0;
            prelaz_obicni_zauzet[i] = false;
        }
    }

    string predji_prelaz(tip_vozila tip, int kolicina_robe_ili_putnika) {   // Funkcija koju pozivaju niti vozila.
        unique_lock<mutex> l(m);
        if (tip == EU_AUTOMOBIL) {                                          // Ukoliko je tip vozila za EU prelaz
            while (prelaz_eu_zauzet) {
                prelaz_eu.wait(l);                                          // Vozilo proba da udje na EU prelaz, ako je zauzet ceka.
            }
            prelaz_eu_zauzet = true;                                        // Zauzima EU prelaz.
            l.unlock();
            this_thread::sleep_for(chrono::seconds(kolicina_robe_ili_putnika)); //Vrsi davanje pasosa.
            l.lock();
            prelaz_eu_zauzet = false;                                       // Oslobadja EU prelaz.
            prelaz_eu.notify_one();                                         // Notificira sledece vozilo iza sebe koje ceka na EU prelaz.
            return "EU";
        } else if (tip == OBICAN_AUTOMOBIL) {
            int broj_prelaza = obicnih_automobila[0] <= obicnih_automobila[1] ? 0 : 1;  // Biranje onog prelaza gde ima manje kola.

            obicnih_automobila[broj_prelaza]++;                             // Povecavanje broja kola na odabranom prelazu.
            while (prelaz_obicni_zauzet[broj_prelaza]) {        
                prelaz_obican[broj_prelaza].wait(l);
            }
            prelaz_obicni_zauzet[broj_prelaza] = true;
            l.unlock();
            this_thread::sleep_for(chrono::seconds(kolicina_robe_ili_putnika));
            l.lock();
            prelaz_obicni_zauzet[broj_prelaza] = false;
            obicnih_automobila[broj_prelaza]--;                             // Smanjivanje broja kola na odabranom prelazu.
            prelaz_obican[broj_prelaza].notify_one();
            return broj_prelaza == 0 ? "OBICAN_NULA" : "OBICAN JEDAN";
        } else if (tip == KAMION) {
            while (prelaz_kamioni_zauzet) {
                prelaz_kamioni.wait(l);
            }
            prelaz_kamioni_zauzet = true;
            l.unlock();
            this_thread::sleep_for(chrono::seconds(kolicina_robe_ili_putnika));
            l.lock();
            prelaz_kamioni_zauzet = false;
            prelaz_kamioni.notify_one();
            return "KAMIONSKI";
        }
    }
};


string vrati_tip_vozila (tip_vozila vozilo) {                               // Funkcija za vracanje stringa u odnosu na tip vozila.
	if (vozilo == EU_AUTOMOBIL) {
		return "EU automobil";
	} else if (vozilo == OBICAN_AUTOMOBIL) {
		return "OBICAN automobil";
	} else {
		return "KAMION";
	}
}

prelaz gp;

void vozilo (tip_vozila tip, int redni_broj_vozila, int kolicina_robe_ili_putnika) {
   static mutex term_m;                                                    // Globalni muteks terminala vidljiv svim nitima.
   {
      unique_lock<mutex> l(term_m);
      cout << "Vozilo broj: " << redni_broj_vozila << " tipa "
           << vrati_tip_vozila(tip) << " doslo na prelaz i nosi " << kolicina_robe_ili_putnika;
      if((tip == EU_AUTOMOBIL) || (tip == OBICAN_AUTOMOBIL)) cout << " putnika." << endl;
      else cout << " tona robe." << endl;
   }
   string prelaz = gp.predji_prelaz(tip, kolicina_robe_ili_putnika);
   {
      unique_lock<mutex> l(term_m);
      cout << "Vozilo broj: " << redni_broj_vozila << " tipa "
           << vrati_tip_vozila(tip) << " preslo prelaz " << prelaz << " (nosio " << kolicina_robe_ili_putnika;
     if((tip == EU_AUTOMOBIL) || (tip == OBICAN_AUTOMOBIL)) cout << "; putnika.)" << endl;
     else          cout << "; tona robe)." << endl;
   }
}

const int VOZILA = 20;

int main() {
   thread t[VOZILA];
   for(int i = 0; i < VOZILA / 4;++i) {
      t[i] = thread(vozilo,EU_AUTOMOBIL, i, rand_sync() % 5 + 1);                 // Rand_sync da bi se dobio razlicit broj putnika i robe.
   }
   for (int i = VOZILA / 4; i < 3 * VOZILA / 4; i++) {
	  t[i] = thread(vozilo,OBICAN_AUTOMOBIL, i, rand_sync() % 5 + 1);
   }
   for (int i = 3 * VOZILA / 4; i < VOZILA; i++) {
	  t[i] = thread(vozilo,KAMION, i, rand_sync() % 5 + 1);
   }
   for(int i = 0; i < VOZILA; ++i) {
      t[i].join();
   }
}

