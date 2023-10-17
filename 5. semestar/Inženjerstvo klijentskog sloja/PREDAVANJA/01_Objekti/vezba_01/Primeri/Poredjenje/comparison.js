console.log('1 == "1"\tis', 1 == '1');			// true
console.log('1 === "1"\tis', 1 === '1');		// false

// Poređenje stringova i brojeva operatorima nejednakosti vrši poredjenje brojeva ako je to moguće.
console.log('1 >= "1"\tis', 1 >= '1');			// true
console.log('1 >= "2"\tis', 1 >= '2');			// false
console.log('11 >= "3"\tis', 11 >= '3');		// true

// Poredjenje stringova relacionim operatorima vrši leksičko poređenje.
console.log('"11" >= "3"\tis', '11' >= '3');    // false

// Poredjenje specijalnih vrednosti
console.log('NaN == NaN\tis', NaN == NaN);      // false
console.log('NaN === NaN\tis', NaN == NaN);     // false

// Poređenje objekata
console.log('{} == {}\tis', {} == {});			// false
console.log('{} === {}\tis', {} === {});		// false
var a = {};
var b = a;
console.log('a == b\t\tis', a == b);			// true

// Poređenje nepoznatih i ne definisanih vrednosti
console.log('null === undefined\tis', null === undefined);	// false
console.log('null == undefined\tis', null == undefined);		// true

// Poređenje boolean i number vrednosti
console.log('false == 0\tis', false == 0);			// true
console.log('false === 0\tis', false === 0);			// false
console.log('true == 1\tis', true == 1);				// true
console.log('false == -1\tis', false == -1);			// false
console.log('true == -1\tis', true == -1);			// false

// Poređenje objekata i primitivnih tipova je moguće, i u tom slučaju se pozivaju metode:
//   valueOf: kada je reč o poređenju objekta i number vrednosti
//   toString: kada je reč o poređenju objekta i string vrednosti
