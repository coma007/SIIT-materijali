'use strict';

(function () {
	var a = 2;

	{
		console.log(3 + 5);
		var _a = 3;
		console.log(_a); // 3
	}

	console.log(a); // 2

	//let i for petlja
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
})();
