/* Naparviti klasu mb (message_box) koja sadrzi n komunikacionih kanala. (n se
 * odredjuje u trenutku instanciranja objekta klase). Komunikacioni kanal
 * (sanduce) omogucava komunikaciju izmedju proizvodjaca i potrosaca nazavisnu
 * od ostalih komunikacija. Svaki kanal moze da sadrzi neogranicen broj poruka.
 *
 * mb ima dve operacije.
 * 1. mb::send() je neblokirajuca operacija sa dva parametra:
 *  - vrednosti (objekt) koja se salje i
 *  - indeksom kanala u koji se salje.
 *
 * 2. mb::receive() je blokirajuca operacija koja prihvata indeks kanala iz 
 *  kojeg ocekuje poruku, a vraca objekt poruke.
 *
 * Jednu poruku je moguce preuzeti samo jednom (pri preuzimanju, poruka se i
 * izbacuje iz sanduceta). Ako u kanalu nema poruke, nit koja je pozvala
 * receive() ceka poruku. Niti koje pozovu receive moraju da dobiju poruke iz
 * odgovarajuceg kanala, ali ne moraju da dobiju poruke u redosledu u kojem su
 * one (poruke) poslate.
 *
 * Operacije send() i receive() bacaju izuzetak ako im se prosledi kanal koji ne
 * postoji.
 *
 * Operacije ove klase su thread safe.
 */
#include <iostream>
#include <queue>
#include <thread>
#include <vector>

using namespace std;

template <typename T, int N> // Templejt klasa. Moze stojati i class umesto typename. N je broj kanala.

class mb {
  vector<queue<T>> data_;           // Vektor redova, pri cemu svaki red moze sadrzati vise poruka tipa T.
  vector<condition_variable *> cv_; // Vektor pokazivaca na uslovne promenljive. Duzina ovog vektora je jednaka duzini
  mutex mx_;                        // vektora data_ (tj. broju kanala). Mora pokazivac na cv.
public:
  mb();
  ~mb();
  void send(T data, int channel);
  T receive(int channel);
};

template <typename T, int N> // Konstruktor klase. Obratiti paznju na sintaksu.
mb<T, N>::mb() {
  for (int i = 0; i < N; ++i) {  // Za svaki od N kanala uraditi sledece:
    data_.push_back(queue<T>{}); // U odgovarajuci element vektora kanala ubaciti novi prazan red. Dati red treba da
                                 // ubuduce prima poruke koje se budu slale i preuzimale.
    cv_.push_back(new condition_variable); // U odgovarajuci element vektora uslovnih promenljivih staviti POKAZIVAC na
  }                                        // novokreiranu uslovnu promenljivu (operacija new). Drugim recima uslovne pro
} // menljive se kreiraju dinamicki na heap-u, a u vektor se stavljaju samo
  // POKAZIVACI na njih. Ovo je uradjeno zato sto uslovne promenljive ne bi mogle
  // da se prenose (kopiraju) u vektor po vrednosti. ZABRANJENO je kopiranje
  // uslovnih promenljivih (operator delete u klasi) kao i mutexa.
template <typename T, int N>
mb<T, N>::~mb() {               // Destruktor klase. Obratiti paznju na sintaksu.
  for (int i = 0; i < N; ++i) { // Za svaki od N kanala uraditi sledece:
    data_.pop_back();           // Iz vektora kanala izabciti red poruka. Efektivno ovim se brisu sve poruke u datom
    delete cv_.back();          // kanalu. Potom se brisu sve uslovne promenljive na koje POKAZUJU pokazivaci koji
    cv_.pop_back();             // se nalaze u vektoru cv_ (operator delete). I na kraju se brisu i sami pokazivaci
  }                             // iz vektora cv_ uz pomoc vektorske operacije pop_back.
}

template <typename T, int N>
void mb<T, N>::send(T data, int channel) { // Funkcija slanja poruke. Prosledjuje se poruka i kanal.
  if (channel >= data_.size())             // Ako je kanal veci od broja kanala, baca se (throw) greska.
    throw out_of_range("Invalid channel index.");

  unique_lock<mutex> l{mx_};  // Ulazak u kriticnu sekciju.
  data_[channel].push(data);  // Ubaci poruku u odgovarajuci kanal
  cv_[channel]->notify_one(); // Probudi potrosaca odgovarajuceg kanala (ako postoji).
}

template <typename T, int N>
T mb<T, N>::receive(int channel) { // Funkcija prijema poruke. Prosledjuje se kanal iz kog se zeli primiti.
  if (channel >= data_.size())     // Ako je kanal veci od broja kanala, baca se (throw) greska.
    throw out_of_range("Invalid channel index.");

  unique_lock<mutex> l{mx_};       // Ulazak u kriticnu sekciju.
  while (data_[channel].empty()) { // Dok nema poruke u kanalu -> cekaj
    cv_[channel]->wait(l);
  }
  T t = data_[channel].front(); // Poruka je stigla. Preuymi poruku sa vrha reda u odgovarajucem kanalu (operacija front).
  data_[channel].pop();         // Nakon preuzimanja izbrisi poruku sa vrha reda.
  return t;
}

mb<char, 3> mb3; // Stvaranje globalnog objekta multi message boxa. Tip poruke je char, ima 3 kanala.

// proizvodjac salje tri uzastopna karaktera pocevsi od prosledjenog karaktera c
void producer(char c, int channel) {
  this_thread::sleep_for(chrono::seconds(1));
  mb3.send(c, channel);
  this_thread::sleep_for(chrono::seconds(1));
  mb3.send(c + 1, channel);
  this_thread::sleep_for(chrono::seconds(1));
  mb3.send(c + 2, channel);
}

// potrosac prima jedan karakter iz odgovarajuceg kanala.
void consumer(int channel) {
  static mutex mx;
  //   this_thread::sleep_for(chrono::seconds(1));
  char c = mb3.receive(channel);
  unique_lock<mutex> l(mx);
  cout << "[" << channel << "]= " << c << endl;
}

const int PROD = 3;
const int CONS = 9;

int main() {
  thread prod[PROD];
  thread cons[CONS];

  // posto svaki proizvodjac posalje tri uzastopna karaktera
  // pocevsi od prosledjenog, znaci da pri ispisu preuzeti karakteri
  // treba da budu (u proizvoljnom redosledu):
  // a,b,c, g,h,i, m,n,o
  char poruke[] = {'a', 'g', 'm'};

  for (int i = 0; i < PROD; ++i)
    prod[i] = thread(producer, poruke[i], i % 3);
  for (int i = 0; i < CONS; ++i)
    cons[i] = thread(consumer, i % 3);
  for (int i = 0; i < PROD; ++i)
    prod[i].join();
  for (int i = 0; i < CONS; ++i)
    cons[i].join();

  return 0;
}
