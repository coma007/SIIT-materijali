// Modelovati skladiste koje ima dve identicne rampe za istovar robe iz kamiona.

// Nosivost kamiona je maksimalno 7 tona.
// Kamioni nose obicnu ili zapaljivu robu.
// Kamioni sa zapaljivom robom imaju prednost pri istovaru.

// Kamion koji zeli da ostavi robu u skladistu poziva operaciju istovari().
// Kamion ceka ispred skadista dok jedna od rampi ne postane slobodna.
// Istovar traje onoliko sekundi koliko u kamionu ima tona robe.
// Operacija istovar() vraca pozivaocu informaciju o tome na kojoj rampi je
// kamion istovaren.

// Stvoriti 5 kamiona sa obicnom i 5 sa zapaljivom robom.

#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

class skladiste {
   bool rampa_slobodna[2];                      // da li su rampe slobodne - po jedan element niza oznacava stanje svake od rampi
   mutex mx;                                    // propusnica za sprecavanje stetnog preplitanja pri pristupu atributima klase
   int zapaljivih;                              // broj kamiona koji cekaju da istovare zapaljivu robu
   condition_variable zapaljivi, obicni;        // uslovne promenljive za modelovanje redova cekanja kamiona koji prevoze zapaljivu robu i onih koji prevoze obicnu robu
public:
   skladiste() : zapaljivih{0} { rampa_slobodna[0]=true; rampa_slobodna[1]=true; } // inicijalno su obe rampe slobodne i nema kamiona sa zapaljivom robom koji cekaju istovar

   int istovari(int kolicina, bool zapaljivo) { // kolicina robe koja se istovara i informacija da li je roba zapaljiva
      unique_lock<mutex> l(mx);                 // zakljucavanje propusnica pre pristupa deljenim promenljivim
      if(zapaljivo)                             // ako prevozi zapaljivu robu, evidentiramo da postoji jos jedan takav kamion
            ++zapaljivih;

      while(rampa_slobodna[0]==false && rampa_slobodna[1]==false) { // dok god su obe rampe zauzete, kamion mora da saceka
      		if (zapaljivo)                // ako prevozi zapaljivu robu, staje u red kamiona koji prevoze tu vrstu robe
               zapaljivi.wait(l);
          else
               obicni.wait(l);                  // ako prevozi obicnu robu, staje u red kamiona koji prevoze tu vrstu robe
      }
      int rampa = rampa_slobodna[0] ? 0 : 1;    // kada se jedna od rampi oslobodila, utvrdjuje se koja je to rampa. Na toj rampi ce kamion izvrsiti istovar
      rampa_slobodna[rampa]=false;              // zauzima rampu na kojoj ce vrsiti istovar
      l.unlock();                               // oslobadjanje propusnice, jer dok je nit u spavanju ne treba sprecavati druge niti da pristupaju deljenim promenljivim
      this_thread::sleep_for(chrono::seconds(kolicina)); // simuliranje istovara robe - istovar traje srazmerno kolicini robe
      l.lock();                                 // ponovo zauzimanje propusnice pre pristupa deljenim promenljivim
      rampa_slobodna[rampa]=true;               // oslobadja se rampa na kojoj je kamion zavrsio istovar
      if(zapaljivo)                             // ako je prevozio zapaljivu robu, jedan takav kamion je sada manje
         --zapaljivih;

      if (zapaljivih)                           // ako ima kamiona koji cekaju da istovare zapaljivu robu, oni imaju prednost, pa se javlja jednom od tih kamiona da izvrsi istovar
         zapaljivi.notify_one();
      else
         obicni.notify_one();                   // ako nema kamiona koji cekaju da istovare zapaljivu robu, onda moze jedan od kamiona koji prevoze obicnu robu da izvrsi istovar
      return rampa;                             // rezultat metode je rampa na kojoj je kamion izvrsio istovar
   }
};

void kamion(skladiste& s, int kolicina, bool zapaljivo) {
   //propusnica za sprecavanje stetnog preplitanja kod pristupa terminalu zbog ispisa. Posto je promenljiva "static", prva nit ce kreirati propusnicu,
   //a sve ostale niti ce koristiti tu istu instancu
   static mutex term_m;
   {
      unique_lock<mutex> l(term_m);
      cout << "Kamion broj: " << this_thread::get_id() << " nosi "
           << kolicina << " tona ";
      if(zapaljivo) cout << "zapaljive robe" << endl;
      else          cout << "obicne robe" << endl;
   }
   int rampa = s.istovari(kolicina, zapaljivo); // istovar robe (uz moguce cekanje ako ispred ima drugih kamiona). Rezultat poziva je rampa na kojoj je izvrsen istovar
   {
      unique_lock<mutex> l(term_m);
      cout << "Kamion broj: " << this_thread::get_id()
           << " istovaren na rampi " << rampa << " (nosio " << kolicina;
     if(zapaljivo) cout << "; zapaljivo)." << endl;
     else          cout << "; obicno)." << endl;
   }
}

const int KAMIONA = 10;
int main () {
   skladiste s{};
   thread t[KAMIONA];
   for(int i = 0; i < KAMIONA; ++i)
      t[i] = thread(&kamion, ref(s), i * 7 % 6 + 1, i % 2); // za kolicinu se svakom kamionu prosledjuje drugacija vrednost koja se izracunava kao i*7%6+1 (da bi bilo maksimalno 7 tona)
   for(int i = 0; i < KAMIONA; ++i)
      t[i].join();
}
