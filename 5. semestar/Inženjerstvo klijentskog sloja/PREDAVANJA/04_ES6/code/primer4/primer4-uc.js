function foo(x,y,z) {
	console.log( x, y, z );
}
foo( ...[1,2,3] ); // 1 2 3
//foo( 1,2,3 ); // 1 2 3

function bar(x, y, ...z) {
console.log( x, y, z );
}
bar( 1, 2, 3, 4, 5 );
//bar( 1, 2, [3,4,5])