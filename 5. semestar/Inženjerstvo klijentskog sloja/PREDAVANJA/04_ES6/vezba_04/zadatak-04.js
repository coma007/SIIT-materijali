// Pre smo default vrednosti postavljali pomocu operatora ||:

var myRide = {
  make: "Ford",
  model: "Model T",
  year: 1959,
  location: "the Office",
  driveTo: function ( place ) {
    this.location = place || "Home"
  }
}

myRide.driveTo("Walmart")
myRide.location // "Walmart"

// vs...

myRide.driveTo()
myRide.location // "Home"


// TODO: Konvertovati driveTo metodu tako da koristi opcionalne parametre.

// Bonus: Kako napraviti da upotrebom starog nacina sa || mozemo da upotrebimo i Boolean vrednosti.
