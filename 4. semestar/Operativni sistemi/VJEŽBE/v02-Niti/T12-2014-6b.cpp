/* Napraviti konkurentni program za izracunavanje obima kruznica. Na pocetku
 * programa korisnik unosi koliko niti treba da se kreira. Svaka nit u svom telu
 * odredjuje poluprecnik kruznice kao pseudoslucajan broj izmedju 1 i 10. Za
 * dobijanje pseudoslucajnog broja izmedju 1 i 10, pozvati rand()%10 + 1
 *
 * Na osnovu generisanog poluprecnika, nit izracunava obim kruznice i u STL
 * kontejner ubacuje redni broj niti i obim kruznice. Za broj PI, koristiti
 * konstantu M_PI iz zaglavlja <cmath>
 *
 * Na kraju glavnog programa, potrebno je ispisati koja nit je generisala
 * najveci obim kruznice.
 *
 * Primer ispisa:
 *
 * Najvecu kruznicu u obimu 50.2655 iscrtala je nit broj 3.
 */
#include <cmath>
#include <iostream>
#include <map>
#include <thread>

using namespace std;

void f(map<int, double> &kruznice, int rbr) {
  int r = rand() % 10 + 1;
  kruznice[rbr] = 2 * r * M_PI;
}

int main() {
  int n;
  cout << "Unesite broj kruznica: ";
  cin >> n;

  map<int, double> kruznice;

  thread *t = new thread[n];
  for (int i = 0; i < n; i++)
    t[i] = thread(f, ref(kruznice), i + 1);

  for (int i = 0; i < n; i++)
    t[i].join();

  map<int, double>::iterator max_it;
  max_it = kruznice.begin();

  for (map<int, double>::iterator it = kruznice.begin(); it != kruznice.end(); it++)
    if (it->second > max_it->second)
      max_it = it;

  cout << "Najvecu kruznicu u obimu: " << max_it->second << " iscrtala je nit " << max_it->first << endl;

  return 0;
}
