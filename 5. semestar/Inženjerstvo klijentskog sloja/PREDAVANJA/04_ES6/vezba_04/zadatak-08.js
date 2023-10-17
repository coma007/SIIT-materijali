// Problem sa sledecim objektom kase je sto bilo ko moze da menja balance. Iako bi to trebalo biti moguce samo kroz
// funkcije deposit i withdraw.

var register = {
  balance: 0,
  deposit: function(value){
    this.balance += value
  },
  withdraw: function(value){
    this.balance -= value
  }
}

register.balance = 100000

// Takodje mozemo i da prosledjujemo podatke pogresnog tipa:

register.deposit(1)
register.deposit("0")
register.deposit("00000")
register.balance

// Promeniti objekat kase tako da koristi gettere i settere (onemoguciti unos).
// Baciti gresku ako je vrednost za sve sto nije pozitivan broj.