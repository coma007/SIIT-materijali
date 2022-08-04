/* Data je klasa Message_box koja predstavlja sanduce za poruke bilo kojeg tipa.
 * Message_box sadrzi dve metode:
 * 1. send(const MESSAGE* message) - za ubacivanje poruke u sanduce i
 * 2. receive() - za preuzimanje poruke iz sanduceta
 *
 * Date su niti proizvodjac i potrosac. Nit proizvodjac ubacuje tri poruke u
 * sanduce, a nit potrosac ih preuzima i ispisuje.
 *
 * Prepraviti klasu tako da bude implementirana u skladu sa sledecim pravilima:
 *  - Nit proizvodjac ne sme da upise novu poruku, dok nit potrosac ne preuzme
 *    prethodno upisan polozaj.
 *  - Nit potrosac ne sme da preuzme polozaj kursora pre nego sto ga nit
 *    proizvodjac upise.
 *  - Nit potrosac ne sme dva puta da preuzme isti polozaj kursora.
 * (Alternativno, koriscenjem stanja:
 *      Nit proizvodjac ne sme da pise u punu deljenu promenljivu.
 *      Nit potrosac ne sme da cita iz prazne deljene promenljive.)
 *
 * Ako program ispravno radi, sve tri poruke trebaju biti preuzete i ispisane,
 * tako da ispis bude:
 *
 *     2
 *     9
 *     7
 */
#include <iostream>
#include <thread>

using namespace std;

template <class MESSAGE> // Genericka klasa (templejt). Moze da prihvati bilo koji tip za neko od svojih polja.
class Message_box {
  mutex mx;
  enum Message_box_states { EMPTY,
                            FULL }; // Stanja sanduceta.
  MESSAGE content;                  // Polje sadrzaja sanduceta. Moze biti bilo kog tipa (class MESSAGE).
  Message_box_states state;         // Trenutno stanje sanduceta.
  condition_variable full;          // Uslovna promenljiva koja sluzi za sinhronizaciju kada se sanduce napuni.
  condition_variable empty;         // Uslovna promenljiva koja sluzi za sinhronizaciju kada se sanduce isprazni.
public:
  Message_box() : state(EMPTY){}; // Na pocetku je sanduce prazno.
  void send(const MESSAGE *message);
  MESSAGE receive();
};

template <class MESSAGE>
void Message_box<MESSAGE>::send(const MESSAGE *message) // Funkcija slanja poruke. Parametar je pokazivac na templejt tip.
{
  unique_lock<mutex> lock(mx);
  while (state == FULL) // Dogod je stanje sanduca FULL (puno) ne moze da se salje nista, tj. mora se prvo isprazniti.
    empty.wait(lock);   // Ceka se na praznjenje sanduceta (od niti koje ga prazne - potrosaci).
  content = *message;   // Sanduce moze da se puni. U sadrzaj se postavlja ono na sta pokazuje pokazivac message.
  state = FULL;         // Stanje je sada puno (FULL).
  full.notify_one();    // Obavestavaju se niti koje su cekale na punjenje sanduceta (potrosaci).
}

template <class MESSAGE>
MESSAGE Message_box<MESSAGE>::receive() {
  unique_lock<mutex> lock(mx);
  while (state == EMPTY) // Dogod je stanje sanduceta EMPTY (prazno) ne moze da se cita nista, tj. mora se prvo napuniti.
    full.wait(lock);     // Ceka se na punjenje sanduceta (od niti koje ga pune - proizvodjaci).
  state = EMPTY;         // Sanduce moze da se prazni. Stanje je sada prazno (EMPTY).
  empty.notify_one();    // Obavestavaju se niti koje su cekale na praznjenje sanduceta (proizvodjaci).
  return content;        // Vracanje sadrzaja. Moze na kraju posto se propusnica pusta tek na samom kraju funkcije.
}

void proizvodjac(Message_box<int> &mb) { // Nit proizvodjaca. Dobija referencu na templejt klasu Message_box.
  int a = 2;
  mb.send(&a); // Salju se tri poruke (2, 9 i 7) globalnom message boxu prosledjenom po referenci.
  a = 9;       // Sekvenca izvrsavanja je send-receive-send-receive-send-receive. Drugim recima
  mb.send(&a); // za svaki send mora ici jedan receive, inace ce program blokirati. Takodje nemoguce
  a = 7;       // je visestruko slanje (bez prijema ili vise prijema bez slanja).
  mb.send(&a);
}

void potrosac(Message_box<int> &mb) {           // Nit potrosaca. Dobija referencu na templejt klasu Message_box.
  cout << "Preuzeto: " << mb.receive() << endl; // 3 receive koji odgovaraju 3 senda iz proizvodjaca. MORA TAKO.
  cout << "Preuzeto: " << mb.receive() << endl;
  cout << "Preuzeto: " << mb.receive() << endl;
}

int main() {
  Message_box<int> mb; // Globalni objekat sanduceta.

  thread t1(proizvodjac, ref(mb)); // Objekat sanduceta prosledjuje se nitima proizvodjaca i potrosaca po referenci.
  thread t2(potrosac, ref(mb));

  t1.join();
  t2.join();

  return 0;
}
