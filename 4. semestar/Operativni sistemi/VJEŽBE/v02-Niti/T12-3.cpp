/* Napraviti konkurentni program koji stvara jednu nit. Nit ima 2 parametra.
 * Jedan je referenca na ulaznu listu a drugi referenca na izlaznu. Nit treba da
 * elemente ulazne liste prebaci u izlaznu tako da stoje u obrnutom redosledu.
 * Ispisati izgled izlazne liste nakon rada niti.
 */
#include <iostream>
#include <list>
#include <thread>

using namespace std;

typedef list<int>::const_iterator Lci; // Deklaracija tipa const interatora na elemente iz liste celobrojnih vrednosti. Lci ce se koristiti kao tip ubuduce.

/*Funkcija koja prima dve liste kao parametre. Jedna lista je lista ulaznih brojeva a druga izlaznih brojeva.
Funkcija treba da elemente jedne liste prebaci u drugu listu i to u obrnutom redosledu.*/
void f(list<int> &in, list<int> &out) {
  for (Lci i = in.begin(); i != in.end(); i++) { // Prolazak kroz ulaznu listu (pomeranje iteratora).
    out.push_front(*i);                          // Stavljanje elementa iz ulazne liste na pocetak izlazne liste.
                        // Ovo efektivno slaze elemente ulazne liste u obrnutom redosledu u izlaznoj listi.
  }
}

int main() {
  list<int> in = {1, 2, 3, 4, 5, 6}; // Ulazna lista brojeva.
  list<int> out;                     // Izlazna lista brojeva (prazna je na pocetku).

  thread t(f, ref(in), ref(out)); // Kreiranje niti od funkcije f. Funkciji se liste prosledjuju po referencama (lista out ce biti menjana pa mora referenca).
  t.join();                       // Cekanje main-a da se nit t zavrsi.

  for (Lci i = out.begin(); i != out.end(); i++) { // Prolazak kroz izlaznu listu i ispisivanje elemenata na ekran.
    cout << *i << " ";
  }

  return 0;
}
