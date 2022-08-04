/* Napraviti konkurentni program koji proverava stanja bankovnih racuna.
 * Bankovni racuni su evidentirani u kontejeneru kao par <kljuc, vrednost> pri
 * cemu je kljuc broj racuna, a vrednost kolicina raspolozivih sredstava na tom
 * racunu. Raspoloziva sredstva su celobrojna vrednost dinara.
 *
 * Provera bankovnih racuna se vrsi u okviru niti. Nit dobija 2 argumenta. Prvi
 * argument je kontejner koji sadrzi <kljuc, vrednost> pri cemu kljuc
 * predstavlja broj racuna koji treba proveriti, a vrednost predstavlja
 * solventnost datog racuna (tj. da li racun ima ili nema dovoljno sredstava).
 * Drugi argument je kontejner prethodno opisanih bankovnih racuna uz pomoc kog
 * nit treba da zakljuci koji su racuni od navedenih u prvom kontejneru
 * solventni a koji nisu i da to zabeleze u okviru prvog kontejnera.
 *
 * Minimalna kolicina novca za solventnost je 5000 dinara. Napraviti 5 bankovnih
 * racuna sa proizvoljnom kolicinom novca na njima i u okviru niti proveriti
 * proizvoljna 3 racuna od tih 5. Na kraju u glavnom programu ispisati stanje
 * solventnosti svakog od ta 3 racuna.
 *
 * Predpostavlja se da korisnik trazi stanje samo postojecih racuna tj. ne trazi
 * stanje racuna koji ne postoji u bazi.
 *
 * Ispis bi trebao da izgleda ovako:
 *
 *     Racun br: 0 je SOLVENTAN
 *     Racun br: 1 je NESOLVENTAN
 *     Racun br: 3 je SOLVENTAN
 *
 * U programu postoji samo jedna nit koja vrsi proveru solventnosti.
 */
#include <iostream>
#include <map>
#include <thread>

#define GRANICA_SOLVENTNOSTI 5000

using namespace std;

string solventnost[2] = {" je NESOLVENTAN", " je SOLVENTAN"};

void provera_solventnosti(map<int, bool> &stanja, map<int, int> &racuni) {
  for (auto it = stanja.begin(); it != stanja.end(); it++) { // prolazak kroz mapu trazenih racuna
    if (racuni[it->first] < GRANICA_SOLVENTNOSTI)            // ukoliko je stanje racuna sa datim kljucem nedovoljno
      it->second = false;                                    // u mapi stanja se postavlja bool na false
    else
      it->second = true; // u suprotnom se postavlja na true
  }
}

int main() {
  map<int, bool> stanja = {make_pair(0, false), make_pair(2, false), make_pair(4, false)};
  map<int, int> racuni = {make_pair(0, 3000), make_pair(1, 6000), // brza inicijalizacija parova kljuc, vrednost
                          make_pair(2, 10000), make_pair(3, 1000), make_pair(4, 5000)};

  thread t(provera_solventnosti, ref(stanja), ref(racuni));
  t.join();

  for (auto it = stanja.begin(); it != stanja.end(); it++) { // ispis solventnosti za svaki od trazenih racuna
    cout << "Racun br: " << it->first << solventnost[it->second] << endl;
  }

  return 0;
}
