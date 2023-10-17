// Koristeci samo jedan literal za objekat, napraviti funkciju car koja vraca ocekivanu vrednost.

function car(make, model, noise){
  return // TODO
}

let auto = car("honda","civic","vroom")
console.log(auto)
// => {make: "honda", model: "civic", drive: Function}
let noise = auto.drive()
console.log(noise)
// => vroom