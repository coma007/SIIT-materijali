/* Napraviti konkurentni program koji radi formiranje evidencije studenata.
 * Studentska sluzba (glavni program) salje 2 kontejnera niti koja formira
 * evidenciju. Prvi kontejner sadrzi indekse studenata, dok drugi kontejner
 * sadrzi ime i prezime studenta (kao jedan element kontejnera). Podrazumeva se
 * da indeks na i-toj poziciji prvog kontejnera odgovara imenu i prezimenu na
 * i-toj poziciji drugog kontejnera.
 *
 * Zadatak niti je da formira novi kontejner koji sadrzi parove
 * <kljuc, vrednost> uz pomoc prethodno opisanih kontenjera brojeva indeksa
 * (kljuc) i imena sa prezimenima (vrednost).
 *
 * Nakon zavrsetka rada niti u glavnom programu ispisati sadrzaj novoformiranog
 * kontejnera sa parovima <kljuc, vrednost>.
 *
 * Ispis bi trebao da izgleda ovako:
 *
 *     Indeks: RA 111/2012 Ime i prezime: Petar Petrovic
 *     Indeks: RA 222/2012 Ime i prezime: Stefan Stefanovic
 *     Indeks: RA 333/2012 Ime i prezime: Milica Micic
 *
 * U programu postoji samo jedna nit koja kreira evidenciju studenata.
 */
#include <iostream>
#include <map>
#include <thread>
#include <vector>

using namespace std;

void evidencija(vector<string> &indeksi, vector<string> &imena_prezimena, map<string, string> &spisak) {
  for (int i = 0; i < indeksi.size(); i++) {
    spisak[indeksi[i]] = imena_prezimena[i]; // kreiranje mape, novi element za svaki indeks
  }
}

int main() {
  vector<string> indeksi = {"RA 111/2012", "RA 222/2012", "RA 333/2012"};
  vector<string> imena_prezimena = {"Petar Petrovic", "Stefan Stefanovic", "Milica Micic"};
  map<string, string> spisak;

  thread t(evidencija, ref(indeksi), ref(imena_prezimena), ref(spisak)); // sve po referecni da se ne bi kopirali veliki
  t.join();                                                              // kontejneri i da bi se izmenila mapa

  cout << "Formirana evidencija:" << endl;
  for (auto it = spisak.begin(); it != spisak.end(); it++) {
    cout << "Indeks: " << it->first << " Ime i prezime: " << it->second << endl;
  }

  return 0;
}
