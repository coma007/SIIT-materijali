/* Napraviti konkurentni program za ispis identifikatora niti sa odredjenim
 * rednim brojem. Na pocetku programa potrebno je pitati korisnika da unese
 * redni broj niti. Program pokrece 10 niti. Svaka nit pri izvrsavanju ispisuje
 * "Pozdrav iz niti X", pri cemu je X redni broj niti. Main funkcija treba da
 * ispise identifikator niti ciji je redni broj korisnik uneo.
 */
#include <iostream>
#include <thread>
#include <vector>

using namespace std;

void f(int rbr) { // Funkcija niti koja ispisuje redni broj niti
  cout << "Pozdrav iz niti " << rbr << endl;
}

int main() {
  int rbr;
  cout << "Unesite redni broj niti: " << endl;
  cin >> rbr;

  thread niti[10]; // Niz od 10 objekata niti.
  for (int i = 0; i < 10; i++) {
    niti[i] = thread(f, i + 1); // Svaki element niza dobija novokreirani objekat.
  }
  cout << "Id niti " << rbr << " je :" << niti[rbr].get_id() << endl; // Na kraju se indeksira element niza sa rbr i ispisuje
                                                                      // se njegov id. Ovo je moguce jer su elementi niza niti.
  for (int i = 0; i < 10; i++)
    niti[i].join();

  return 0;
}
