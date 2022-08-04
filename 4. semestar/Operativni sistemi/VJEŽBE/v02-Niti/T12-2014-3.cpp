/* Napraviti konkurentni program koji racuna srednju vrednost elemenata vektora.
 * Racunanje srednje vrednosti se vrsi tako sto se izracunaju parcijalne sume
 * elemenata vektora koje se saberu u glavnoj niti i u istoj niti se racuna
 * srednja vrednost. Parcijalne sume prve 2 trecine vektora izracunaju 2 niti
 * kreirane iz glavnog programa, dok parcijalnu sumu trece trecine vektora treba
 * da izracuna nit main. OBEZBEDITI DA SE SVA TRI RACUNA IZVRSAVAJU KONKURENTNO!
 *
 * Nakon sto su izracunate sve 3 parcijalne sume, glavna nit treba da ih sabere
 * i izracuna srednju vrednost svih elemenata vektora.
 *
 * Broj elemenata vektora ne mora biti deljiv sa 3. Elementi vektora su tipa 
 * double.
 */
#include <iostream>
#include <thread>
#include <vector>

using namespace std;

typedef vector<double>::const_iterator vci;

void izracunaj_sumu(vci pocetak, vci kraj, double &suma) {
  suma = 0;
  for (auto it = pocetak; it != kraj; it++) {
    suma += *it;
  }
}

int main() {
  vector<double> v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  vector<double> sume(3);
  double srednja = 0;
  thread t[2];

  vci pocetak = v.begin();
  vci kraj = pocetak + v.size() / 3;
  for (int i = 0; i < 2; i++) {
    t[i] = thread(izracunaj_sumu, pocetak, kraj, ref(sume[i])); // 2 niti dobijaju odgovarjuce iteratore
    pocetak += v.size() / 3;
    kraj += v.size() / 3;
  }
  izracunaj_sumu(pocetak, v.end(), sume[2]); // nit main racuna KONKURENTNO svoju sumu sa druge dve niti

  for (int i = 0; i < 2; i++) {
    t[i].join();
  }

  for (int i = 0; i < sume.size(); i++) {
    srednja += sume[i];
  }

  cout << "Srednja vrednost svih elemenata vektora je: " << srednja / v.size() << endl;

  return 0;
}
