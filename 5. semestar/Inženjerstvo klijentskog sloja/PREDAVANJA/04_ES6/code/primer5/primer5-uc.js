function bar(val) {
  console.log( "bar called!" );
  return y + val;
}
function foo(x = y + 3, z = bar( x )) {
  console.log( x, z );
}
var y = 5;
foo(); // "bar called"
// 8 13
foo( 10 ); // "bar called"
// 10 15
y = 6;
foo( undefined, 10 ); // 9 10