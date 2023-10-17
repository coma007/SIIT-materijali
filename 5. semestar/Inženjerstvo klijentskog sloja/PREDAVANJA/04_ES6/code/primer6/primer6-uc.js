//ES5
function foo() {
  return [1,2,3];
}
var tmp = foo(), a = tmp[0], b = tmp[1], c = tmp[2];
console.log( a, b, c );

function bar() {
  return {
    x: 4,
    y: 5,
    z: 6
  };
}
var tmp = bar(), x = tmp.x, y = tmp.y, z = tmp.z;
console.log( x, y, z );

//ES6
//destrukturiranje
var [ a, b, c ] = foo();
var { x: x, y: y, z: z } = bar();
console.log( a, b, c ); // 1 2 3
console.log( x, y, z ); // 4 5 6

//delimicna dodela destrukturiranjem
var [,,c,d] = foo();
var { w, z } = bar(); 
//var { w:w, z:z } = bar(); 
console.log( c, z ); // 3 6
console.log( d, w ); // undefined undefined

//spread/rest i destrukturiranje
var a = [2,3,4];
var [b, ...c] = a;
console.log( b, c ); // 2 [3,4]

//default vrednosti i destrukturiranje
var [ a = 3, b = 6, c = 9, d = 12 ] = foo();
var { x = 5, y = 10, z = 15, w:WW = 20 } = bar();
console.log( a, b, c, d ); // 1 2 3 12
console.log( x, y, z, WW ); // 4 5 6 20

//destrukturiranje parametara funkcije
function f1( [ x, y ] ) {
	console.log( x, y );
}
f1( [ 1, 2 ] ); // 1 2
f1( [ 1 ] ); // 1 undefined
f1( [] ); // undefined undefined

function f2( { x, y } ) {
	console.log( x, y );
}
f2( { y: 1, x: 2 } ); // 2 1
f2( { y: 42 } ); // undefined 42
f2( {} ); // undefined undefined