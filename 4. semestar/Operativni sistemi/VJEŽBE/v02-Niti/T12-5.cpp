/* Napraviti konkurentni program koji pravi srpsko engleski recnik iz englesko
 * srpskog recnika. Recnik ima proizvoljan broj reci (bitno je da bude vise od
 * jedne). Posao treba obaviti u jednoj niti. Ispisati englesko srpski i srpsko
 * engleski recnik na kraju programa.
 *
 * Napomena: ispis prevedenih reci ne mora biti u redosledu unesenih reci
 * prilikom formiranja recnika, ali prevod mora biti tacan.
 */
#include <iostream>
#include <map>
#include <thread>

using namespace std;

typedef map<string, string>::const_iterator Mci;

void swap_words(map<string, string> &englesko_srpski, map<string, string> &srpsko_engleski) { // Funkcija za kreiranje srpsko_engleskog recnika iz engelsko_srpskog.
  for (Mci i = englesko_srpski.begin(); i != englesko_srpski.end(); i++) {                    // Prolazak iteratorom kroz citav englesko_srpski recnik.
    srpsko_engleski[i->second] = i->first;                                                    // Zamena kljuceva i vrednosti jednog i drugog recnika (swap), sto efektivno dovodi do stvaranja srpsko_engelskog recnika.
  }
}

int main() {
  string engleski[10] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"};   // Niz engleskih reci.
  string srpski[10] = {"jedan", "dva", "tri", "cetiri", "pet", "sest", "sedam", "osam", "devet", "deset"}; // Niz srpskih reci.
  map<string, string> englesko_srpski;                                                                     // Recnik (mapa) engleskih reci sa srpskim prevodom.
  map<string, string> srpsko_engleski;                                                                     // Recnik (mapa) srpskih reci sa engleskim prevodom.

  for (int i = 0; i < 10; i++) {
    englesko_srpski[engleski[i]] = srpski[i]; // Stvaranje engelsko_srpskog recnika.
  }

  thread t(swap_words, ref(englesko_srpski), ref(srpsko_engleski)); // Kreiranje niti koja vrsi stvaranje srpsko_engelskog recnika preko funkcije swap_words.
  t.join();

  cout << "ENGLESKO-SRPSKI:" << endl;
  for (Mci i = englesko_srpski.begin(); i != englesko_srpski.end(); i++) { // Ispis engelsko_srpskog recnika.
    cout << i->first << " : " << i->second << endl;
  }

  cout << "SRPSKO-ENGLESKI:" << endl;
  for (Mci i = srpsko_engleski.begin(); i != srpsko_engleski.end(); i++) { // Ispis srpsko_engelskog recnika.
    cout << i->first << " : " << i->second << endl;
  }

  return 0;
}
