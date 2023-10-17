"use strict";

var _get = function get(object, property, receiver) { if (object === null) object = Function.prototype; var desc = Object.getOwnPropertyDescriptor(object, property); if (desc === undefined) { var parent = Object.getPrototypeOf(object); if (parent === null) { return undefined; } else { return get(parent, property, receiver); } } else if ("value" in desc) { return desc.value; } else { var getter = desc.get; if (getter === undefined) { return undefined; } return getter.call(receiver); } };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

//--"klasa"
var Foo = function () {
  function Foo(a, b) {
    _classCallCheck(this, Foo);

    this.x = a;
    this.y = b;
  }

  _createClass(Foo, [{
    key: "gimmeXY",
    value: function gimmeXY() {
      return this.x * this.y;
    }
  }]);

  return Foo;
}();

var f = new Foo(5, 15);
console.log(f.x); // 5
console.log(f.y); // 15
console.log(f.gimmeXY()); // 75

//--"nasledjivanje"

var Bar = function (_Foo) {
  _inherits(Bar, _Foo);

  function Bar(a, b, c) {
    _classCallCheck(this, Bar);

    var _this = _possibleConstructorReturn(this, (Bar.__proto__ || Object.getPrototypeOf(Bar)).call(this, a, b));

    _this.z = c;
    return _this;
  }

  _createClass(Bar, [{
    key: "gimmeXYZ",
    value: function gimmeXYZ() {
      return _get(Bar.prototype.__proto__ || Object.getPrototypeOf(Bar.prototype), "gimmeXY", this).call(this) * this.z;
    }
  }]);

  return Bar;
}(Foo);

var b = new Bar(5, 15, 25);

console.log(b.x);
console.log(b.y);
console.log(b.z);
console.log(b.gimmeXYZ());
console.log(b.gimmeXY());

//--static

var Baz = function () {
  function Baz() {
    _classCallCheck(this, Baz);
  }

  _createClass(Baz, [{
    key: "f",
    value: function f() {
      console.log("function call");
    }
  }], [{
    key: "cool",
    value: function cool() {
      console.log("cool");
    }
  }]);

  return Baz;
}();

Baz.answer = 42;

var Buz = function (_Baz) {
  _inherits(Buz, _Baz);

  function Buz() {
    _classCallCheck(this, Buz);

    var _this2 = _possibleConstructorReturn(this, (Buz.__proto__ || Object.getPrototypeOf(Buz)).call(this));

    console.log(new.target.answer);
    return _this2;
  }

  return Buz;
}(Baz);

console.log(Baz.answer); // 42
console.log(Buz.answer); // 42
var b = new Buz(); // 42
console.log(b.f());
// console.log(b.cool()); // cool is not a function
// console.log(b.answer); // undefined -- `answer` is static on `Foo`
