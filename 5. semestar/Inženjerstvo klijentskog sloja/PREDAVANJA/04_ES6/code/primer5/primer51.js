"use strict";

var f = function f() {
    var x = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : 11;
    var y = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 31;

    return x + y;
};
