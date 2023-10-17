"use strict";

var _slicedToArray = function () { function sliceIterator(arr, i) { var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"]) _i["return"](); } finally { if (_d) throw _e; } } return _arr; } return function (arr, i) { if (Array.isArray(arr)) { return arr; } else if (Symbol.iterator in Object(arr)) { return sliceIterator(arr, i); } else { throw new TypeError("Invalid attempt to destructure non-iterable instance"); } }; }();

function _toArray(arr) { return Array.isArray(arr) ? arr : Array.from(arr); }

function foo() {
  return [1, 2, 3];
}
var tmp = foo(),
    a = tmp[0],
    b = tmp[1],
    c = tmp[2];
console.log(a, b, c);

function bar() {
  return {
    x: 4,
    y: 5,
    z: 6
  };
}
var tmp = bar(),
    x = tmp.x,
    y = tmp.y,
    z = tmp.z;
console.log(x, y, z);

//destrukturiranje

var _foo = foo(),
    _foo2 = _slicedToArray(_foo, 3),
    a = _foo2[0],
    b = _foo2[1],
    c = _foo2[2];

var _bar = bar(),
    x = _bar.x,
    y = _bar.y,
    z = _bar.z;

console.log(a, b, c); // 1 2 3
console.log(x, y, z); // 4 5 6

//delimicna dodela destrukturiranjem

var _foo3 = foo(),
    _foo4 = _slicedToArray(_foo3, 4),
    c = _foo4[2],
    d = _foo4[3];

var _bar2 = bar(),
    w = _bar2.w,
    z = _bar2.z;

console.log(c, z); // 3 6
console.log(d, w); // undefined undefined

//spread/rest i destrukturiranje
var a = [2, 3, 4];

var _a = _toArray(a),
    b = _a[0],
    c = _a.slice(1);

console.log(b, c); // 2 [3,4]

//default vrednosti i destrukturiranje

var _foo5 = foo(),
    _foo6 = _slicedToArray(_foo5, 4),
    _foo6$ = _foo6[0],
    a = _foo6$ === undefined ? 3 : _foo6$,
    _foo6$2 = _foo6[1],
    b = _foo6$2 === undefined ? 6 : _foo6$2,
    _foo6$3 = _foo6[2],
    c = _foo6$3 === undefined ? 9 : _foo6$3,
    _foo6$4 = _foo6[3],
    d = _foo6$4 === undefined ? 12 : _foo6$4;

var _bar3 = bar(),
    _bar3$x = _bar3.x,
    x = _bar3$x === undefined ? 5 : _bar3$x,
    _bar3$y = _bar3.y,
    y = _bar3$y === undefined ? 10 : _bar3$y,
    _bar3$z = _bar3.z,
    z = _bar3$z === undefined ? 15 : _bar3$z,
    _bar3$w = _bar3.w,
    WW = _bar3$w === undefined ? 20 : _bar3$w;

console.log(a, b, c, d); // 1 2 3 12
console.log(x, y, z, WW); // 4 5 6 20

//destrukturiranje parametara funkcije
function f1(_ref) {
  var _ref2 = _slicedToArray(_ref, 2),
      x = _ref2[0],
      y = _ref2[1];

  console.log(x, y);
}
f1([1, 2]); // 1 2
f1([1]); // 1 undefined
f1([]); // undefined undefined

function f2(_ref3) {
  var x = _ref3.x,
      y = _ref3.y;

  console.log(x, y);
}
f2({ y: 1, x: 2 }); // 2 1
f2({ y: 42 }); // undefined 42
f2({}); // undefined undefined
