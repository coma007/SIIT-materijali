class Student(object):
    """
    U ovoj implementaciji klase student prosek računamo 'lenjo' (lazily).
    Lenjo računanje se odnosi na situaciju kada neku operaciju ili proračun
    (ovde proseka) obavimo ne što je pre moguće, nego kada nam zatreba,
    odnosno u poslednjem trenutku.

    Polazimo od toga da se najverovatnije ocene mnogo češće upisuju i brišu u
    odnosu na potrebu za pristupom proseku. Postavlja se pitanje da li možemo da
    proredimo računanje proseka? Možemo, jer je prosek potrebno računati jedino
    kada se pozove get metoda za prosek pa poziv metode za računanje proseka
    izmeštamo u getter.

    Primetićemo da je vrednost proseka veći deo vremena neažurna, odnosno ne
    odgovara realnom proseku ocena.
    """
    def __init__(self, ime, prezime):
        self._ime = ime
        self._prezime = prezime
        self._diplomirao = False
        self._prosek = 0
        self._ocene = []

    def get_ime(self):
        return self._ime

    def set_ime(self, ime):
        self._ime = ime

    def get_prezime(self):
        return self._prezime

    def set_prezime(self, prezime):
        self._prezime = prezime

    def get_prosek(self):
        self._racunaj_prosek()
        return self._prosek

    def ispis_podataka(self):
        print("Student " + self._ime + " " + self._prezime + " ima prosek " + str(self._prosek))

    def _racunaj_prosek(self):
        suma = 0
        broj = 0
        for ocena in self._ocene:
            suma += ocena
            broj += 1

        self._prosek = suma/broj

    def upis_ocene(self, nova_ocena):
        self._ocene.append(nova_ocena)

    def ponistavanje_ocene(self, ocena):
        self._ocene.remove(ocena)
