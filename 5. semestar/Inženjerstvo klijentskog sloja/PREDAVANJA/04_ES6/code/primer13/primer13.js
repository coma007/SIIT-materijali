(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});
var foo = 42;
var baz = function baz() {
	return 'first value';
};
exports.default = { foo: foo };
var bar = exports.bar = "hello world";
exports.baz = baz;
//obzirom da se eksportuje BINDING objekta
//a ne vrednost objekta,
//kasnije izmene (bez obzira odakle se vrse)
//ODRAZICE SE na importovane vrednost

foo = 10;
exports.bar = bar = "cool";
exports.baz = baz = function baz() {
	return 'second value';
};

},{}],2:[function(require,module,exports){
'use strict';

var _dummyModule = require('./dummyModule');

var dummy = _interopRequireWildcard(_dummyModule);

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }

console.log('foo:', dummy.default); // import {default as foo, bar, baz} from './dummyModule';

console.log('bar:', _dummyModule.bar);
console.log('baz:', (0, _dummyModule.baz)());

console.log('default:', dummy.default);
console.log('baz:', dummy.baz());

},{"./dummyModule":1}]},{},[2]);
