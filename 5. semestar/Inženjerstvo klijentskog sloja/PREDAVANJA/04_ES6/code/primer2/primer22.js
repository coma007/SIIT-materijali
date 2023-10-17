'use strict';

var funcs = [];

for (var i = 0; i < 5; i++) {
    (function (i) {
        funcs.push(function () {
            console.log('var i: ', i);
        });
    } (i));
}
funcs[3]();
