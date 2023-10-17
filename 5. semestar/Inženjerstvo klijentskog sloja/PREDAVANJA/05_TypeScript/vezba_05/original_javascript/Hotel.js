(function() {
  // TODO 1: Napraviti java objekat Adresa koji ima sledeca polja:
  //    grad:     string
  //    drzava:   string
  //    nazivUlice: string
  //    broj:     number
  //
  //      Implementirati toString metodu da ispisuje nesto smisleno.
  var Adresa = function Adresa(grad, drzava, nazivUlice, broj) {
    this.grad = grad;
    this.drzava = drzava;
    this.nazivUlice = nazivUlice;
    this.broj = broj;

    return this;
  };
  Adresa.prototype.toString = function() {
    return this.drzava + ', ' + this.grad + ', ' + this.nazivUlice + ' ' +this.broj;
  };
  // Eksportovanje funkcije
  modeli.HotelAdresa = Adresa;

  // TODO 2: Napraviti java objekat Hotel koji ima sledeca polja:
  //    adresa:       Adresa
  //    naziv:        string
  //    slobodneSobe:     Array{number}
  //    rezervisaneSobe:  Objekat gde je kljuc broj sobe, a vrednost osoba koja je rezervisala tu sobu.
  //
  //    Dodati funkciju koja rezervise sobu. Izbaciti Izuzetak u slucaju da soba nije slobodna. Parametri funkcije (brojSobe, podaciSobe)
  //    Dodati funkciju koja oslobadja sobu i vraca podatke o sobi.
  //    Dodati funkciju koja vraca ukupan broj soba u hotelu
  //      Implementirati toString metodu da ispisuje nesto smisleno.
  var Hotel = function Hotel(adresa, naziv, slobodneSobe) {
    this.adresa = adresa;
    this.naziv = naziv;
    this.slobodneSobe = slobodneSobe;
    this.rezervisaneSobe = {};

    return this;
  };
  Hotel.prototype.rezervisi = function(brojSobe, podaciSobe) {
    var idx = this.slobodneSobe.indexOf(brojSobe);
    if (idx !== -1) {
      this.slobodneSobe.splice(idx, 1);
      this.rezervisaneSobe[brojSobe] = podaciSobe;
    } else {
      throw {
        name: 'Rezervacija',
        message: 'Soba ' + brojSobe + ' nije slobodna.'
      }
    }
  };
  Hotel.prototype.oslobodi = function(brojSobe) {
    var retVal;
    if (brojSobe in this.rezervisaneSobe) {
      retVal = this.rezervisaneSobe[brojSobe];
      delete this.rezervisaneSobe[brojSobe];
      this.slobodneSobe.push(brojSobe);
    }
    return retVal;
  };
  Hotel.prototype.brojSoba = function() {
    return this.slobodneSobe.length + Object.keys(this.rezervisaneSobe).length;
  };
  Hotel.prototype.toString = function() {
    var retVal = 'Hotel "' + this.naziv + '" na adresi "' + this.adresa + '" ima slobodne sobe: ' + JSON.stringify(this.slobodneSobe) + ' i rezervisane sobe:\n';
    for (var broj in this.rezervisaneSobe) {
      retVal += '\t' + broj + ': ' + this.rezervisaneSobe[broj];
    }
    return retVal;
  };
  modeli.Hotel = Hotel;
})();