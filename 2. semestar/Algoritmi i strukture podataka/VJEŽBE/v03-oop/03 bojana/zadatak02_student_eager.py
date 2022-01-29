class Student(object):
    """
    U ovoj implementaciji klase student prosek računamo 'vredno' ili
    'nestrpljivo' (eagerly).
    Eager računanje se odnosi na situaciju kada neki proračun (ovde proseka)
    obavimo što je pre moguće uz konstantno održavanje ažurne vrednosti.
    """

    def __init__(self, ime, prezime):
        self._ime = ime
        self._prezime = prezime
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
        self._racunaj_prosek()

    def ponistavanje_ocene(self, ocena):
        self._ocene.remove(ocena)
        self._racunaj_prosek()
