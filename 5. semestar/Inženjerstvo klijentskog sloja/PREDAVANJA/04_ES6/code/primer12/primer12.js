'use strict';

var _marked = /*#__PURE__*/regeneratorRuntime.mark(foo),
    _marked2 = /*#__PURE__*/regeneratorRuntime.mark(bar);

//Generator
function foo() {
  var x;
  return regeneratorRuntime.wrap(function foo$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          if (!true) {
            _context.next = 7;
            break;
          }

          _context.next = 3;
          return Math.random();

        case 3:
          x = _context.sent;

          console.log('x:', x);
          _context.next = 0;
          break;

        case 7:
        case 'end':
          return _context.stop();
      }
    }
  }, _marked, this);
}

var it = foo();

for (var i = 0; i < 10; i++) {
  var v = it.next(i);
  console.log('v:', v);
};

//--Delegiranje yield iteratoru
function bar() {
  return regeneratorRuntime.wrap(function bar$(_context2) {
    while (1) {
      switch (_context2.prev = _context2.next) {
        case 0:
          return _context2.delegateYield([1, 2, 3], 't0', 1);

        case 1:
        case 'end':
          return _context2.stop();
      }
    }
  }, _marked2, this);
}

it = bar();

for (i = 0; i < 4; i++) {
  v = it.next();
  console.log('v:', v);
};
