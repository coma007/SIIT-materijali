"use strict";

var o = {
  x: 1,
  m: function m() {
    var _this = this;

    var f = function f() {
      console.log(_this);
    };
    f();
  }
};
