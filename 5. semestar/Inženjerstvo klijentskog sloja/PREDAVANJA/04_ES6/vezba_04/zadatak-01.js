// Popraviti kod, u ES6 i ES5 tako da pozivi callbacks funkcija ispisuju ocekivane vrednosti.

"use strict"

var callbacks = []
for (var i = 0; i < 10; i++) {
  callbacks.push(function() { console.log(i) })
}

callbacks[2]()
