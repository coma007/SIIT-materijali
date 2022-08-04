/* Napraviti konkurentni program koji simulira serijalizaciju objekata u JSON
 * format pri slanju podataka sa veb servera na klijent. JSON objekti se sastoje
 * od parova <kljuc,vrednost>.
 *
 * U main funkciji, koriscenjem odgovarajuceg STL kontejnera, definisati JSON
 * objekat Korisnik koji ima sledece parove:
 *
 *     <id,1>
 *     <ime,Marko>
 *     <prezime,Markovic>
 *     <email,marko.markovic@gmail.com>
 *
 * Zatim napraviti posebnu nit koja ispisuje sadrzaj JSON objekta u JSON
 * formatu.
 *
 * Ispis u JSON formatu izgleda ovako:
 *
 *     {"email":"marko.markovic@gmail.com","id":"1","ime":"Marko","prezime":"Markovic"}
 *
 * Pri ispisu nije vazan redosled parova.
 */
#include <iostream>
#include <map>
#include <thread>

using namespace std;

void obrada(map<string, string> &z) {
  string s = "{";
  for (auto it = z.begin(); it != z.end(); it++)
    s += "\"" + it->first + "\":\"" + it->second + "\",";
  s[s.length() - 1] = '}';

  cout << s << endl;
}

int main() {
  map<string, string> zahtev;

  zahtev["id"] = "1";
  zahtev["ime"] = "Marko";
  zahtev["prezime"] = "Markovic";
  zahtev["email"] = "marko.markovic@gmail.com";

  thread t(obrada, ref(zahtev));
  t.join();

  return 0;
}
