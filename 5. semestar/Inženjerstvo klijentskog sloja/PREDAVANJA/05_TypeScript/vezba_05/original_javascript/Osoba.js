(function() {
  // TODO 3: Implementirati objekat Adresa koja ce se koristiti za objekte Osoba.
  //      nazivUlice:   string
  //      brojZgrade:   number
  //      brojStana:    number 
  //
  //      Implementirati toString metodu
  var Adresa = function Adresa(nazivUlice, brojZgrade, brojStana) {
    this.nazivUlice = nazivUlice;
    this.brojZgrade = brojZgrade;
    this.brojStana = brojStana;

    return this;
  };
  Adresa.prototype.toString = function() {
    return this.nazivUlice + ' ' + this.brojZgrade + ' ' + this.brojStana;
  };
  modeli.OsobaAdresa = Adresa;

  // TODO 4: Implementirati objekat Osoba
  //      ime:        string
  //      prezime:      string
  //      adresaStanovanja:   Adresa
  //
  //      Implementirati metodu koja rezervise hotel i snima podatke u polje "rezervacija" oblika:
  //      {
  //        hotel: <instanca hotela>,
  //        broj: <broj rezervisane sobe>
  //      }
  //      Implementirati metodu koja oslobadja rezervisanu sobu.
  //      Implementirati toString metodu
  var Osoba = function Osoba(ime, prezime, adresaStanovanja) {
    this.ime = ime;
    this.prezime = prezime;
    this.adresaStanovanja = adresaStanovanja;

    return this;
  };
  Osoba.prototype.rezervisi = function(hotel, broj) {
    var self = this;
    try {
      hotel.rezervisi(broj, self);
      self.rezervacija = {
        hotel: hotel,
        soba: broj
      }
    } catch(e) {
      console.log(e);
    }
  };
  Osoba.prototype.oslobodi = function() {
    var rezervacija = this.rezervacija;
    rezervacija.hotel.oslobodi(rezervacija.soba);
  };
  Osoba.prototype.toString = function() {
    return this.ime + ' ' + this.prezime + ' sa adrese "' + this.adresaStanovanja + '"';
  };
  modeli.Osoba = Osoba;
})();
