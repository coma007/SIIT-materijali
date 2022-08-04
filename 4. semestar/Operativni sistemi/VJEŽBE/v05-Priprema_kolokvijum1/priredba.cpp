/*
Napraviti konkurentni program koji bira najviseg ucenika i najvisu ucenicu
iz razreda, koji ce na skolskoj priredbi predstavljati svoj razred.
(Bilo bi logicno da se traze najlepsi - u pitanju je priredba, ali ne znam 
kako se meri lepota. I zato trazimo najvise.)

Ucenici (oba pola) su modelovani nitima nastalim od funkcije ucenik.
Pri stvaranju niti se zadaje pol i visina ucenika.
Podrazumeva se da u razredu ne postoje dva ucenika iste visine.
Svaki ucenik poziva operaciju prijava(),
koja vraca true ucenicima koji su izbrani, a false ostalima.

Organizator priredbe (funkcija main) poziva operaciju predstavnici() 
koja vraca identifiktore ucenika koji su izabrani 
da budu predstavnici razreda na priredbi.
Organizator ispisuje identifikatore izabranih ucenika.

Napomena:
main poziva operaciju predstavnici() _pre_ join(), a ispisuje 
predstavnike _posle_ join().
*/

#include <thread>
#include <iostream>
#include <map>
#include <mutex>
#include <condition_variable>

using namespace std;

enum Pol {M, Z};
class Priredba {
    mutex m;
    condition_variable svi_prijavljeni[2];                  // CV kao indikator da su svi ucenici jednog od polova prijavljeni.
    condition_variable izabrani;                            // CV na kojoj se ceka da se izaberu najvisi ucenici.
    unsigned ucenika[2];                                    // Broj decaka i devojcica.
    map<unsigned, thread::id> visine[2];                    // Mapa decaka i devojcica. Kljuc je visina a vrednost ID ucenika.
public:
    Priredba(unsigned decaka_, unsigned devojcica_) {       // Konstruktor zadaje koliko ima decaka i devojcica na pocetku.
        ucenika[M] = decaka_;
        ucenika[Z] = devojcica_;
    }
    bool prijava(Pol pol, unsigned visina) {                // Funkcija koju zove nit ucenik. Prosledjuje se pol kao i visina ucenika.
        unique_lock<mutex> l(m);
        visine[pol][visina] = this_thread::get_id();        // U odgovarajucu mapu u odgvarajuci kljuc (po visini) se upisuje id.
        if(--ucenika[pol] == 0) {                           // Ukoliko je broj prijavljenih ucenika porastao do max broja ucenika za
            svi_prijavljeni[pol].notify_all();              // taj pol, javi da su svi prijavljeni, takodje javi da su predstavnici
            izabrani.notify_one();                          // izabrani.
        }
        while(ucenika[pol] != 0) {                          // Ako nisam zadnji ucenik koji je prijavljen, cekam da dodje zadnji i javi.
            svi_prijavljeni[pol].wait(l);
        }
        return visine[pol].crbegin()->second == this_thread::get_id();  // Vrati 0 ili 1 u zavisnosti da li je moja visina
    }                                                                   // visina najveceg (da li je id, id najviseg).
    std::pair<thread::id, thread::id> predstavnici() {
        unique_lock<mutex> l(m);
        while((ucenika[M] != 0) || (ucenika[Z] != 0)) {     // Dogod nisu svi prijavljeni cekaj.
            izabrani.wait(l);
        }
        return make_pair(visine[M].crbegin()->second,       // Kada jesu prijavljeni napravi par najvisih iz muske i zenske mape.
                         visine[Z].crbegin()->second);      // Map operator sortiranja sortira kljuc sa < tj. levo su manji
    }                                                       // a desno veci elementi. Tako da je skroz na kraju najveci kljuc.
};

void ucenik(Priredba& priredba, Pol pol, unsigned visina) {
    static mutex term;
    {
        unique_lock<mutex> l(term);
        cout << this_thread::get_id() << " : Pol " << (pol==M ? "M" : "Z")
             << ", visina " << visina << ". Prijavljujem se..."  << endl;
    }
    auto izabran_sam = priredba.prijava(pol, visina);           //0 ako nije izabran 1 ako jeste.
    {
        unique_lock<mutex> l(term);
        cout << this_thread::get_id() << " : Pol " << (pol==M ? "M" : "Z")
             << ", visina " << visina << ". "
             << (izabran_sam ? "JUUUUHUU!" : "Rasticu ja jos...") << endl;
    }
}

const unsigned UCENIKA = 10;
int main() {
    Priredba priredba(UCENIKA/2, UCENIKA/2);
    thread t[UCENIKA];
    for(auto i=0u; i<UCENIKA; ++i)
        t[i] = thread(ucenik, ref(priredba), static_cast<Pol>(i%2), i);
        
    auto p = priredba.predstavnici();           //Moraju se odabrati pobednici pre nego sto se ispisu nakon join-a. Takodje
                                                //ovo je komunikacija izmedju niti ucenik i organizatora (main). Ne bi mogla
    for(auto i= 0u; i < UCENIKA; ++i)              //da postoji komunikacija nakon zavrsetka niti ucenik.
        t[i].join();
            
    cout << "Predstavnici su: " << p.first << " i " << p.second << endl;    //2 polja pair objekta (first i second).   
}
