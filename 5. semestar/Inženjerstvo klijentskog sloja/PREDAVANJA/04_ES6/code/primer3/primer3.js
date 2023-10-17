'use strict';

var funcs = [];

var _loop = function _loop(i) {
	funcs.push(function () {
		console.log('let: ', i);
	});
};

for (var i = 0; i < 5; i++) {
	_loop(i);
}
funcs[3](); // 3
//----------------------------------
var funcs1 = [];
for (var i1 = 0; i1 < 5; i1++) {
	funcs1.push(function () {
		console.log('var: ', i1);
	});
}
funcs1[3](); // 5
