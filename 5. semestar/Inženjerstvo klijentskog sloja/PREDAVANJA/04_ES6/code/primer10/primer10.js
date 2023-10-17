'use strict';

var _obj;

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var MY_KEY = Symbol();
var FOO = Symbol();
var obj = (_obj = {}, _defineProperty(_obj, MY_KEY, 123), _defineProperty(_obj, FOO, function () {
    return 'bar';
}), _obj);
console.log(obj[MY_KEY]); //123
console.log(obj[FOO]()); //bar


var COLOR_RED = Symbol('Red');
var COLOR_ORANGE = Symbol('Orange');
var COLOR_YELLOW = Symbol('Yellow');
var COLOR_GREEN = Symbol('Green');
var COLOR_BLUE = Symbol('Blue');
var COLOR_VIOLET = Symbol('Violet');

function getComplement(color) {
    switch (color) {
        case COLOR_RED:
            return COLOR_GREEN;
        case COLOR_ORANGE:
            return COLOR_BLUE;
        case COLOR_YELLOW:
            return COLOR_VIOLET;
        case COLOR_GREEN:
            return COLOR_RED;
        case COLOR_BLUE:
            return COLOR_ORANGE;
        case COLOR_VIOLET:
            return COLOR_YELLOW;
        default:
            throw new Exception('Unknown color: ' + color);
    }
}

console.log(getComplement(COLOR_BLUE));
