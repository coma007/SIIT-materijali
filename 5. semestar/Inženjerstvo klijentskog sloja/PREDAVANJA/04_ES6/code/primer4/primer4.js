"use strict";

function foo(x, y, z) {
	console.log(x, y, z);
}
foo.apply(undefined, [1, 2, 3]); // 1 2 3

function bar(x, y) {
	for (var _len = arguments.length, z = Array(_len > 2 ? _len - 2 : 0), _key = 2; _key < _len; _key++) {
		z[_key - 2] = arguments[_key];
	}

	console.log(x, y, z);
}
bar(1, 2, 3, 4, 5);
