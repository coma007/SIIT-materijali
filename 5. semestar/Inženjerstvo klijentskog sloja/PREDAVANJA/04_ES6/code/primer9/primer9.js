'use strict';

function Prefixer(prefix) {
    this.prefix = prefix;
}
Prefixer.prototype.prefixArray = function (arr) {
    var that = this; // zbog cega nam treba ova linija koda?
    return arr.map(function (x) {
        return that.prefix + x;
    });
};

//------------------------------------------------------------
//Arrow funkcije
var pre = new Prefixer('Hi ');
console.log(pre.prefixArray(['Joe', 'Alex']));

function PrefixerA(prefix) {
    this.prefix = prefix;
}

PrefixerA.prototype.prefixArray = function (arr) {
    var _this = this;

    return arr.map(function (x) {
        return _this.prefix + x;
    });
};

pre = new PrefixerA('Hi ');
console.log(pre.prefixArray(['Joe', 'Alex']));
