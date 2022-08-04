/* Napraviti konkurentni program za simulaciju logovanja na udaljeni racunar.
 *
 * Da bi se logovao, u glavnom programu korisnik redom treba da unese:
 *
 *     login <enter>
 *     <korisnicko_ime> <enter>
 *     <lozinka> <enter>
 *
 * Nakon toga posebna nit treba da utvrdi da li korisnik moze da se uloguje.
 *
 * Provera ispravnosti logovanja vrsi se na osnovu evidencije korisnika. U
 * glavnom programu, koriscenjem STL kontejnera, evidentirati sledece korisnike:
 *
 *     1. korisnicko_ime: milan, lozinka: 12345
 *     2. korisnicko_ime: marko, lozinka: xyz
 *     3. korisnicko_ime: admin, lozinka: 4dm1n
 *
 * Nit treba da utvrdi da li je najpre unesena rec "login". Ako jeste, korisnik
 * se moze ulogovati ako postoji evidentiran korisnik sa unesenim  korisnickim
 * imenom i lozinkom.
 *
 * Ako je logovanje uspesno, nit ispisuje:
 *
 *     Korisnik uspesno prijavljen.
 *
 * U slucaju neuspesnog logovanja, nit ispisuje:
 *
 *     Neuspesna prijava!
 */
#include <iostream>
#include <map>
#include <thread>

using namespace std;

void login(string *s, map<string, string> &korisnici) {
  if (s[0] == "login" && korisnici.find(s[1]) != korisnici.end() && korisnici[s[1]] == s[2])
    cout << "Korisnik uspesno ulogovan";
  else
    cout << "Neispravno korisnicko ime ili lozinka!";
}

int main() {
  map<string, string> korisnici;
  korisnici["milan"] = "12345";
  korisnici["marko"] = "xyz";
  korisnici["admin"] = "4dm1n";

  string s[3];
  for (int i = 0; i < 3; i++) {
    getline(cin, s[i]);
  }

  thread t(login, s, ref(korisnici));
  t.join();

  return 0;
}
