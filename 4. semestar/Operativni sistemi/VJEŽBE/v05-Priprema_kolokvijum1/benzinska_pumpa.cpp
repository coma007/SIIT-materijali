// Modelovati benzinsku pumpu na kojoj se toce 3 vrste goriva:
// bezolovni, dizel i super.
// Svako vozilo koje zeli da natoci gorivo mora da stane u red za tu vrstu goriva.
// Tocenje bezolovnog traje 1 sekundu, dizela 2, a supera 3 sekunde.

// Vozilo koje zeli da natoci gorivo poziva operaciju natoci() i prosledjuje joj
// vrstu goriva koja mu je potrebna.

// Treba stvoriti po 4 vozila za svaku vrstu goriva.

// Komentari su obavezni.

#define _GLIBCXX_USE_NANOSLEEP

#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

class benzinska_pumpa
{
      mutex m;                                              // propusnica za pristup iskljucivom regionu
      condition_variable bds[3];                            // redovi cekanja za bezolovni, dizel i super, redom
      bool bds_busy[3];                                     // informacija da li su zauzete tocilice za bezolovni, dizel i super, redom
public:
      enum vrsta_goriva
      {
            BEZOLOVNI = 0,
            DIZEL,
            SUPER
      }; //tipovi goriva
      benzinska_pumpa();
      void natoci(vrsta_goriva gorivo);
};

benzinska_pumpa::benzinska_pumpa()
{ //inicijalno su sve tocilice slobodne
      bds_busy[0] = false;
      bds_busy[1] = false;
      bds_busy[2] = false;
}

void benzinska_pumpa::natoci(vrsta_goriva gorivo)
{                                                           // parametar je gorivo koje zelimo da natocimo
      unique_lock<mutex> l(m);                              // pre pristupa deljenim resursima, trazimo propusnicu
      while (bds_busy[gorivo])                              // dok god tocilica za trazenu vrstu goriva nije slobodna, nit mora da ceka
            bds[gorivo].wait(l);
      bds_busy[gorivo] = true;                              // zauzima tocilicu za svoju vrstu goriva
      l.unlock();                                           // dok traje tocenje, nema razloga da se drzi propusnica i onemoguci drugim nitima da pristupaju deljenim promenljivim u klasi
      this_thread::sleep_for(chrono::seconds(gorivo + 1));  // simuliranje trajanja tocenja srazmerno tipu goriva
      l.lock();
      bds_busy[gorivo] = false;                             // oslobadjanje tocilice za svoju vrstu goriva
      bds[gorivo].notify_one();                             // javljamo jednom iz reda koji zeli da natoci istu vrstu goriva da se tocilica oslobodila
}

string naziv_goriva(benzinska_pumpa::vrsta_goriva gorivo)
{
      if (gorivo == benzinska_pumpa::BEZOLOVNI)
            return "bezolovni";
      else if (gorivo == benzinska_pumpa::SUPER)
            return "super";
      else
            return "dizel";
}

void vozilo(benzinska_pumpa &pumpa, benzinska_pumpa::vrsta_goriva gorivo)
{
      static mutex term_m;
      {
            unique_lock<mutex> l(term_m);
            cout << "Vozilu " << this_thread::get_id()
                 << " je potreban " << naziv_goriva(gorivo) << "." << endl;
      }
      pumpa.natoci(gorivo);
      unique_lock<mutex> l(term_m);
      cout << "Vozilo " << this_thread::get_id()
           << " je natocilo " << naziv_goriva(gorivo) << "." << endl;
}

const int AUTOMOBILA = 12;
int main()
{
      benzinska_pumpa p;
      thread t[AUTOMOBILA];
      for (int i = 0; i < AUTOMOBILA; ++i)
            t[i] = thread(vozilo, ref(p), (benzinska_pumpa::vrsta_goriva)(i % 3)); //po 4 automobila toce svaku od vrsta goriva
      for (int i = 0; i < AUTOMOBILA; ++i)
            t[i].join();
}
