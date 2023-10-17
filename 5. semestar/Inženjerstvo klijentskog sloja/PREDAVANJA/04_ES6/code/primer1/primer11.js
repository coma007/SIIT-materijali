"use strict";

var foo = [1, 2, 3];
var obj = {
	foo: foo // means 'foo: foo'
};
console.log(obj.foo); // [1,2,3]
