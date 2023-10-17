// Istinitosne vrednosti za number tip
console.log('0 is:', 0 ? 'Truthy' : 'Falsy');
console.log('1 is:', 1 ? 'Truthy' : 'Falsy');
console.log('-1 is:', -1 ? 'Truthy' : 'Falsy');

// Istinitosne vrednosti za string tip
console.log('Empty string is:', '' ? 'Truthy' : 'Falsy');
console.log('NonEmpty string is:', 'random string' ? 'Truthy' : 'Falsy');

// Istinitosne vrednosti objekata
console.log('Empty object {} is:', {} ? 'Truthy' : 'Falsy');
console.log('undefined is:', undefined ? 'Truthy' : 'Falsy');
console.log('null is:', null ? 'Truthy' : 'Falsy');
var foo = function() {};
console.log('function is:', foo ? 'Truthy' : 'Falsy');


// Dodela na osnovu istinitosnih vrednosti
var a; // Samo deklaracija, vrednost je undefined
var b = {message: 'bVariable'};

var c = a || b.message;
console.log('Vrednost promenljive c:', c);

b = {};
var z = a || b.message || 'Default Message';
console.log('Vrednost promenljive z:', z);
