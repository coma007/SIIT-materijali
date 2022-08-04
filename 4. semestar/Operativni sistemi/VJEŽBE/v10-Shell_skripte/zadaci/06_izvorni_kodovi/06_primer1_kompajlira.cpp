/*Napraviti konkurentni program koji stvara nit iz koje:
pita korisnika za visinu u centimetrima i
ispisuje: “Vasa visina je <uneta_visina> cm.”

Testirati program tako sto ce se nit prevesti iz stanja 
joinable prvo operacijom join a nakon toga detach.
*/

#include<iostream>
#include<thread>

using namespace std;
using namespace thread;
void kod_niti() {               //Funkcija niti.
  int visina;
  cout << "Unesite vasu visinu u cm:" << endl;
  cin >> visina;
  cout << "Vasa visina je: " << visina << " cm" << endl;
}
int main() {
   thread nit(kod_niti);       //Stvaranje niti i pokretanje niti.
   nit.join();                 //Cekanje niti main da se zavrsi nit t.
   //nit.detach();             //Nit main NE ceka da se zavrsi nit t (detach se koristi kod niti koje sadrze beskonacne petlje - deamon niti).
}




