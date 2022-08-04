/* 
Napraviti konkurentni program koji simulira ponasanje kernela operativnog sistema pri dodeli 2-jezgarnog procesora nitima.
Niti pokusavaju da zauzmu jedno od jezgara procesora. Ukoliko je bar jedno jezgro slobodno, ono se dodeljuje niti na
koriscenje odredjeni vremenski period delta koji iznosi 1 sekundu. Ukoliko su oba jezgra zauzeta nit ceka na jezgru na 
kome ceka manje niti (kako bi se raspodelilo opterecenje). 

Nakon koriscenja jezgra delta (1) sekundi nit prepusta jezgro nekoj drugoj niti koja ceka za njegovo koriscenje 
(bilo da je u pitanju nit koja je tek dosla na cekanje ili neka druga nit kojoj je bio istekao vremenski period delta)
i ulazi u cooldown (cekanje pre ponovnog pokusaja zauzimanja procesora kako bi se dala sansa drugim nitima da koriste 
procesor).

Nakon cooldown perioda (10 ms) nit ponovo pokusava da zauzme procesor. Data sekvenca zauzimanje-otpustanje procesora 
se izvrsava minimalno jednom ili vise puta u zavisnosti koliko sekundi nit pokusava da koristi procesor.

Da bi se ispratio rad programa potrebno zabeleziti trenutak pocetka koriscenja (nakon zauzimanja) procesora od strane 
niti kao i trenutak kraja koriscenja procesora. Dati trenuci se koriste u niti radi izracunavanja trajanja operacije 
koriscenja procesora.

Kreirati 1 procesor i 10 niti. Svaka nit treba da pokusava da zauzme procesor proizvoljan vremenski
period od 1-4 sekunde. 

Napomena: Obratiti paznju da nit u toku rada ne mora uvek zauzimati isto jezgro procesora.

Komentari su obavezni.
*/

#include <thread>
#include <iostream>
#include <mutex>
#include <condition_variable>

#define DELTA 1
#define COOLDOWN 10

using namespace std;
using namespace chrono;

struct vremena {
	steady_clock::time_point pocetak;
	steady_clock::time_point kraj;
};

class Procesor {
	int broj_niti[2];                           // Brojaci niti koje cekaju na jedno od dva jezgra
	bool jezgro_zauzeto[2];                     // Indikator da li neko jezgro trenutno opsluzuje nit
	condition_variable jezgro_cv[2];            // CV na kojima se ceka na pristup nekom od jezgara
	mutex m;
public:
	Procesor() {
		for (int i = 0; i < 2; i++) {
			broj_niti[i] = 0;
			jezgro_zauzeto[i] = false;
		}
	}
	
	vremena zauzmi_procesor(int sekundi) {      // Funkcija zauzeca procesora koju pozivaju niti
		int br_jezgra = 0;                      // Promenljiva u koju se smesta koje je jezgro odabrano
		bool poceo = false;                     // Indikator pocetka rada niti na jezgru.
		vremena vr;
		for (int i = 0; i < sekundi; i++) {     // Koliko sekundi ima toliko sekundi nit zauzima i oslobadja jezgra.
			{
				unique_lock<mutex> l(m);
				br_jezgra = (broj_niti[0] < broj_niti[1]) ? 0 : 1;  // Zauzima se ono jezgro na kojem ceka manji broj niti.
				broj_niti[br_jezgra]++;                             // Povecava se broj niti koje cekaju na datom jezgru.
				while  (jezgro_zauzeto[br_jezgra]) {
					jezgro_cv[br_jezgra].wait(l); 
				}
				if (!poceo) {
					vr.pocetak = steady_clock::now();               // Belezi se pocetak samo pri prvom prolazu
					poceo = true;
				}
				jezgro_zauzeto[br_jezgra] = true;                   // Zauzimanje jezgra
			}
			this_thread::sleep_for(seconds(DELTA));                 // Koriscenje jezgra
			{
				unique_lock<mutex> l(m);
				broj_niti[br_jezgra]--;                             // Smanjenje broja niti na jezgru
				jezgro_zauzeto[br_jezgra] = false;                  // Oslobadjanje jezgra
				jezgro_cv[br_jezgra].notify_one();                  // Notifikacija sledeceg
			}
			this_thread::sleep_for(milliseconds(COOLDOWN));         // Neophodan cooldown da damo sansu drugim nitima da dobiju jezgro.	
		}
		vr.kraj = steady_clock::now();
		return vr;
	}
};

mutex term_mx;

void nit(Procesor & p, int rbr, int sekundi) {
	vremena vr = p.zauzmi_procesor(sekundi);
	double multiplier = 1;
	if (sekundi > 1)  multiplier = 1.01;        // Multiplier u ocekivano vreme dodaje i vreme cooldown perioda.
	duration<double> s = vr.kraj - vr.pocetak;

	unique_lock<mutex> l(term_mx);
	cout << "Nit broj: " << rbr << " provela u cekanju i koriscenju procesora: " 
		 << s.count() << " sekundi od planiranih: " << sekundi*multiplier << " sekundi." 
		 << endl;
}

int br_niti = 10;

int main () {
	thread niti[br_niti];
	Procesor p;
	srand(time(NULL));                          // Seed random generatora zavisi od sistemskog vremena (uvek razlicit random brojevi).
	for (int i = 0; i < br_niti; i++) {
		niti[i] = thread(nit, ref(p), i, (rand()%4+1));
	}
	for (int i = 0; i< br_niti; i++) {
		niti[i].join();
	}
}
