/* Napraviti program koji kreira jednu nit i 
u okviru nje ispisuje proizvoljnu recenicu*/

#include<iostream>
#include<thread>

using namespace std;
using namespace thread;
void kod_niti() {               //Funkcija niti.
   cout << "Pozdrav iz niti!" << endl;
}

int main() {
	thread t(kod_niti);         /*Stvaranje objekta niti (t) od funkcije kod_niti(), i pokretanje niti. 
	                              Objekat niti (t) efektivno predstavlja samu nit, pa cemo ubuduce 
	                              objekat niti zvati samo nit radi lakseg shvatanja komentara.*/
	t.join();                   //Poziv operacije join() na niti t. Nit main ceka da se nit t zavrsi.
}
