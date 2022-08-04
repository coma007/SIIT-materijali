/* Napisati program za unos reci sa tastature sa ukljucenom proverom ispravnosti
 * unosa. Dat je vektor recnik koji predstavlja reci koje sistem prepoznaje kao
 * ispravne. Funkcija proveri_ispravnost() utvrdjuje da li se prosledjena rec
 * nalazi u recniku.
 *
 * U glavnom programu korisnik unosi jednu po jednu rec. Nakon unosa reci, u
 * posebnoj niti se vrsi provera ispravnosti reci.
 *
 * Kada korisnik zavrsi unos svih reci, za svaku rec se ispisuje da li je
 * ispravno unesena.
 *
 * Primer ispisa:
 *
 *     Rec 1 ispravno napisana.
 *     Rec 2 neispravno napisana.
 *     Rec 3 ispravno napisana.
 */
#include <iostream>
#include <string>
#include <thread>
#include <vector>

using namespace std;

vector<string> recnik{"black", "red", "blue", "yellow", "white"}; // reci koje spell-checker prepoznaje

void proveri_ispravnost(string rec, bool *rez) {
  // u recniku se trazi prosledjena rec
  *rez = false;
  for (vector<string>::iterator it = recnik.begin();
       it != recnik.end(); it++) {
    if (*it == rec) {
      *rez = true;
      break;
    }
  }
}

int main() {
  vector<thread *> niti;    // vektor niti u kojima ce se vrsiti provera ispravnosti podataka
  vector<bool *> rezultati; // niz rezultata izvrsavanja niti. Elementi su pokazivaci jer bi se vrednost kopirala pri ubacivanju u vektor, tako da se ne bi videla promena nad elementom izvrsena od strane niti
  string rec;

  while (getline(cin, rec)) { // unosi se rec sa tastature i smesta u promenljivu rec
    // buduci rezultat smestamo u vektor
    rezultati.push_back(new bool);
    // kreiramo nit i ubacujemo je u vektor
    niti.push_back(new thread(proveri_ispravnost, rec, rezultati[rezultati.size() - 1]));
  }

  int i = 0;
  for (vector<thread *>::iterator it = niti.begin(); it != niti.end(); it++) {
    (*it)->join();
  }

  for (int i = 0; i < rezultati.size(); i++) {
    bool ispravna = *(rezultati[i]);
    cout << "Rec " << i << " napisana: "
         << (ispravna == true ? "ispravno" : "neispravno") << endl;
  }

  return 0;
}
