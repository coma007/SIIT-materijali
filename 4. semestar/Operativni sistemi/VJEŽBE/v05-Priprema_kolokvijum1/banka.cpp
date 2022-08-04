// Napraviti konkurentni program koji modeluje kreditno poslovanje banke.
// Banka odobrava kredite u dinarima i u evrima.

// Klijent trazi kredit pozivanjem operacije uzmi_kredit(),
// kojoj prosledjuje svotu koju zeli da pozajmi od banke i valutu u kojoj zeli da pozajmi.
// Klijent neko vreme koristi pozajmljena sredstva, pa ih vrati banci
// pozivanjem operacije vrati_kredit().

// Banka inicijalno poseduje odredjene svote dinara i evra
// na dva razlicita racuna, koje pozajmljuje.
// Banka odobrava kredite dok ima sredstava.
// Kada vise nema sredstava, banka ceka da klijenti vrate
// pretodno odobrene kredite pre nego sto odobri sledeci kredit.
// Banka odobrava kredite u proizvoljnom redosledu.

// Banka tezi tome da klijent ciji je zahtev moguce ispunitini
// (postoje sredstva) ne ceka na kredit.

// Komentari su obavezni

// Obrisati main i implementaciju banke (ostaviti enum).

//#define _GLIBCXX_USE_NANOSLEEP
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

class banka
{
    int dsaldo, esaldo;                                 // ukupno novca u banci na dinarskom, odnosno deviznom racunu
    mutex m;                                            // propusnica za pristup deljenim resursima
    condition_variable dlikvidan, elikvidan;            // redovi cekanja za uzimanje kredita u dinarima, odnosno u evrima
public:
    enum valute
    {
        DINAR = 0,
        EVRO
    };                                                  // tipovi valuta
    banka(int inicijalni_dsaldo, int inicijalni_esaldo) // inicijalni saldo se prosledjuje spolja pri kreiranju objekta klase banka
        : dsaldo(inicijalni_dsaldo), esaldo(inicijalni_esaldo)
    {
    }
    int uzmi_kredit(int svota, valute valuta);
    int vrati_kredit(int svota, valute valuta);
};

int banka::uzmi_kredit(int svota, valute valuta)
{                                                       // parametar je svota koja se uzima kredit i valuta u kojoj se uzima
    unique_lock<mutex> l(m);                            // trazimo propusnicu pre pristupa deljenim promenljivim
    int saldo;                                          // lokalna promenljiva u koju cemo upisati ono sto treba da bude povratna vrednost funkcije
    if (valuta == DINAR)
    {                                                   // ako trazimo kredit u dinarima
        while (dsaldo < svota)                          // dok god nema trazene kolicine dinara na racunu banke, klijent mora da saceka
            dlikvidan.wait(l);
        dsaldo -= svota;                                // smanjujemo ukupnu kolicinu dinara u banci, jer se trazeni iznos daje klijentu
        saldo = dsaldo;                                 // postavljanje povratne vrednosti
    }
    else
    {                                                   // ako je kredit trazen u evrima
        while (esaldo < svota)                          // dok god nema trazene kolicine evra na racunu banke, klijent mora da saceka
            elikvidan.wait(l);
        esaldo -= svota;                                // smanjujemo ukupnu kolicinu evra u banci, jer se trazeni iznos daje klijentu
        saldo = esaldo;                                 // postavljanje povratne vrednosti
    }

    return saldo;
}

int banka::vrati_kredit(int svota, valute valuta)
{                                                       // parametar je svota koja se vraca i valuta u kojoj se vraca
    int saldo;                                          // lokalna promenljiva u koju cemo upisati ono sto treba da bude povratna vrednost funkcije
    unique_lock<mutex> l(m);                            // trazimo propusnicu pre pristupa deljenim promenljivim
    if (valuta == DINAR)
    {                                                   // ako vracamo kredit u dinarima
        dsaldo += svota;                                // povecavamo ukupnu kolicinu dinara u banci, jer je klijent vratio novac u banku
                                                        // javljamo svima koji cekaju dinare da se pojavila nova kolicina novca u banci.
                                                        // Novi saldo u banci je za neke klijente dovoljan da bi dobili kredit, a za neke je i dalje taj saldo premali
                                                        // Da se ne bi desilo da pozivom notify_one() probudimo nekog od klijenata kojima je i novi iznos salda i dalje premali
                                                        // (u toj varijanti bi program otisao u beskonacno cekanje, jer bi se probudjeni klijent vratio u cekanje zbog nedostatka novca
                                                        // a druge klijente niko ne bi probudio), budimo sve klijente. Medju njima ce biti bar jedan koji ce moci da dobije kredit,
                                                        // a ostali ce ponoo otici u cekanje
        dlikvidan.notify_all();
        saldo = dsaldo;                                 // postavljanje povratne vrednosti
    }
    else
    {                                                   // ako je rec o evrima, sve se ponavlja analogno vracanju kredita u dinarima
        esaldo += svota;
        elikvidan.notify_all();
        saldo = esaldo;
    }

    return saldo;
}

string naziv_valute(banka::valute valuta)
{
    if (valuta == banka::DINAR)
        return "dinar";
    else
        return "evro";
}

void klijent(banka &b, int svota, banka::valute valuta)
{
    static mutex term_m;
    thread::id id = this_thread::get_id();
    int saldo;
    {
        unique_lock<mutex> l(term_m);
        cout << "Klijent: " << id << " trazi na zajam " << svota
             << ", valuta: " << naziv_valute(valuta) << endl;
    }
    saldo = b.uzmi_kredit(svota, valuta);
    {
        unique_lock<mutex> l(term_m);
        cout << "Klijent: " << id << " dobio " << svota
             << ", u banci ostalo: " << saldo
             << ", valuta: " << naziv_valute(valuta) << endl;
    }
    // klijent koristi pozajmljeni novac
    this_thread::sleep_for(chrono::seconds(1));
    saldo = b.vrati_kredit(svota, valuta);
    unique_lock<mutex> l(term_m);
    cout << "Klijent: " << id << " vratio " << svota
         << ", u banci ostalo: " << saldo
         << ", valuta: " << naziv_valute(valuta) << endl;
}

const int DSVOTA = 30;
const int ESVOTA = 20;
const int KLIJENATA = 18;

int main()
{
    banka b{DSVOTA, ESVOTA};
    thread t[KLIJENATA];
    for (int i = 0; i < KLIJENATA; ++i)
        t[i] = thread(klijent, ref(b),
                      1 + i * 3 % (DSVOTA < ESVOTA ? DSVOTA : ESVOTA), // svota se odredjuje na neki polu-slucajan nacin, zavisno od brojaca i. Vazno je samo da svaki klijent trazi razlicite kolicine novca, da imamo i klijente koji traze u dinarima, kao i one koji traze u evrima, i da niko ne trazi vise novca nego sto ukupno ima u banci
                      (banka::valute)(i % 2));
    for (int i = 0; i < KLIJENATA; ++i)
        t[i].join();
}
