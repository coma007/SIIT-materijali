/* Napraviti thread-safe jednostruko spregnutu listu ciji cvorovi sadrze cele
 * brojeve. Testirati rad liste datim glavnim programom.
 */
#include <iostream>
#include <mutex>
#include <random>
#include <thread>

using namespace std;

// klasa koja predstavlja jedan cvor liste
class ListNode {
private:
  ListNode *next; // cvor ima pokazivac na njemu naredni cvor
  int content;    // sadrzaj cvora je neki ceo broj
public:
  ListNode(ListNode *n, int c) : next(n), content(c) {} // pri konstruisanju se prosledi pokazivac na sledeci i sadrzaj
  ListNode *getNext() const { return next; }            // getter za sledeci cvor
  void setNext(ListNode *n) { next = n; }               // setter za sledeci cvor
  int getContent() const { return content; }            // getter za sadrzaj
};

// Klasa predstavlja jednostruko spregnutu listu
class LinkedList {
private:
  ListNode *first; // lista ima pokazivac na svoj prvi cvor
  int size;        // ukupan broj elemenata u listi (zbog optimizacije, da ne bi stalno morali da prebrojavamo)
  mutex m;         // propusnica za sprecavanje stetnog preplitanja u operacijama liste
public:
  LinkedList() : first(NULL), size(0) {}      // inicijalno nema elemenata
  void addElement(int content);               // dodavanje na kraj liste novog cvora u listu sa prosledjenim sadrzajem
  void deleteElement();                       // brisanje prvog cvora liste
  void insertElement(int content, int index); // ubacivanje novog cvora u listu na poziciju specificiranu parametrom "index"
  ~LinkedList();
  friend ostream &operator<<(ostream &os, LinkedList &list) { // ispis elemenata liste u stream
    unique_lock<mutex> l(list.m);
    ListNode *temp = list.first;       // pozicioniramo se na prvi element
    while (temp != NULL) {             // redom prolazimo kroz listu
      os << temp->getContent() << " "; // ispisujemo sadrzaj trenutnog cvora
      temp = temp->getNext();          // pomerimo se na naredni cvor
    }
    return os;
  }
};

void LinkedList::addElement(int content) {
  // zakljucamo propusnicu da bi sprecili stetno preplitanje.
  // Ako ovo ne bismo uradili, rad niti bi mogao biti prekinut u toku izvrsavanja funkcije sto bi moglo imati za posledicu neispravan rad funkcije
  unique_lock<mutex> l(m);
  ListNode *newNode = new ListNode(NULL, content); // kreiramo novi cvor i u njega ubacimo prosledjeni sadrzaj
  if (first == NULL) {                             // ako nema nijednog cvora
    first = newNode;                               // proglasimo novi cvor prvim i jedinim cvorom u listi
  } else {                                         // ako ima cvorova
    ListNode *temp = first;                        // pozicioniramo se na prvi cvor
    while (temp->getNext() != NULL) {              // redom prolazimo kroz sve elemente do kraja
      temp = temp->getNext();
    }
    temp->setNext(newNode); // uvezemo novi cvor nakon poslednjeg cvora u listi
  }
  size++; // sada ima jedan element vise u listi
}

void LinkedList::insertElement(int content, int index) {
  if (index < size) {                                // indeks mora biti u skladu sa velicinom liste
    unique_lock<mutex> l(m);                         // zakljucamo propusnicu da bi sprecili stetno preplitanje
    ListNode *newNode = new ListNode(NULL, content); // kreiramo novi cvor
    if (first == NULL) {                             // ako je lista prazna
      first = newNode;                               // novi cvor je prvi i jedini cvor
    } else {                                         // ako ima elemenata
      ListNode *temp = first;                        // pozicioniramo se na prvi cvor
      for (int i = 0; i < index; ++i)                // pomeramo se redom do cvora sa rednim brojem "indeks"
        temp = temp->getNext();

      newNode->setNext(temp->getNext()); // na poziciju na kojoj smo zavrsili pomeranje uvezujemo novi cvor (veza novog cvora sa njemu narednim)
      temp->setNext(newNode);            // veza prethodnog cvora sa novim cvorom
    }
    size++; // sada ima jedan element vise u listi
  }
}

void LinkedList::deleteElement() {
  unique_lock<mutex> l(m);                            // zakljucamo propusnicu da bi sprecili stetno preplitanje
  if (first != NULL) {                                // ako ima bar jedan element u listi
    ListNode *forDelete = first;                      // pozicioniramo se na prvi element
    this_thread::sleep_for(chrono::milliseconds(10)); // simuliranje pauze da bi se desilo preplitanje. Ako region nije zakljucan propusnicom, ovde moze doci do stetnog preplitanja
    first = first->getNext();                         // Izvezemo prvi element iz liste
    delete forDelete;                                 // obrisemo memoriju koju zauzima element koji smo izbacili iz liste
    size--;                                           // sada ima jedan element manje u listi
  }
}

LinkedList::~LinkedList() { // pri unistavanju liste redom brisemo elemente, jer se u funkciji "deleteElement" oslobadja memorija koju zauzimaju elementi
  while (first != NULL)
    deleteElement();
}

void add(LinkedList &l) { // slobodna funkcija koja dodaje 10 elemenata u listu
  for (int i = 0; i < 10; i++) {
    l.addElement(i);
  }
}

void insert(LinkedList &l) { // slobodna funkcija koja ubacuje 10 elemenata u listu na slucajne pozicije
  random_device rd;
  uniform_int_distribution<int> ceo_broj(0, 99);
  for (int i = 0; i < 10; i++) {
    l.insertElement(i, ceo_broj(rd));
  }
}

void del(LinkedList &l) { // slobodna funkcija koja 10 puta poziva brisanje prvog elementa liste
  for (int i = 0; i < 10; i++) {
    l.deleteElement();
  }
}

int main() {
  LinkedList list;
  add(list);

  // pravimo dve niti od koje obe 10 puta pozivaju brisanje prvog elementa. Ukoliko dodje do stetnog preplitanja, brisanje se nece uspesno izvrsiti
  thread t1(del, ref(list));
  thread t2(del, ref(list));

  t1.join();
  t2.join();

  cout << list; // ispis svih elemenata liste

  return 0;
}
