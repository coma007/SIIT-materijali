"use strict";

function bar(val) {
  console.log("bar called!");
  return y + val;
}
function foo() {
  var x = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : y + 3;
  var z = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : bar(x);

  console.log(x, z);
}
var y = 5;
foo(); // "bar called"
// 8 13
foo(10); // "bar called"
// 10 15
y = 6;
foo(undefined, 10); // 9 10
