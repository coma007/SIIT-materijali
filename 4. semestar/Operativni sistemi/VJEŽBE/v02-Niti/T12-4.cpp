/* Napraviti konkurentni program koji pronalazi element najblizi 0 iz zadatog
 * niza brojeva. Posao podeliti tako da ga izvrsavaju 3 niti. Duzina niza
 * brojeva treba da je deljiva sa 3.
 */
#include <cmath>
#include <iostream>
#include <thread>

using namespace std;

void f(double *a, int n, double *min) { // Funkcija za trazenje minimalnog elementa u okviru niza. Od funkcije ce biti pravljene niti.
  *min = a[0];                          // Mimimum se inicijalizuje na prvi element niza.
  for (int i = 1; i < n; ++i) {
    if (abs(a[i]) < abs(*min)) // Ako je element po apsolutnoj vrednosti manji od mimimuma po apsolutnoj vrednosti onda taj element postaje minimum.
      *min = a[i];
  }
}

int main() {
  int n = 3;
  int length = 9; // Broj elemenata niza treba da bude deljiv sa brojem niti (npr 9 elemenata i 3 niti).
  double a[] = {1, 2, 3, 4, 0.5, 6, -0.3, 8, 9};
  double minimumi[n]; // Niz od 3 mimimuma (svaka nit racuna jedan minimum).

  thread *niti = new thread[n];
  for (int i = 0; i < n; ++i) {
    niti[i] = thread(f, a + i * (length / 3), length / 3, &minimumi[i]); // Kreiranje niti. Svaka nit dobija odgovarajuci deo niza, tj. pokazivac na odgovarajuci deo niza a.
  }

  for (int i = 0; i < n; ++i) {
    niti[i].join();
  }

  double rez = minimumi[0]; // Nakon racunanja 3 minimuma u nitima, racuna se globalni miminum u main-u, po istoj logici kao i funkciji f.
  for (int i = 1; i < n; i++) {
    if (abs(minimumi[i]) < abs(rez))
      rez = minimumi[i];
  }

  delete[] niti;

  cout << "Najblizi element nuli je: " << rez << endl; // Ispis globalnog minimuma.

  return 0;
}
