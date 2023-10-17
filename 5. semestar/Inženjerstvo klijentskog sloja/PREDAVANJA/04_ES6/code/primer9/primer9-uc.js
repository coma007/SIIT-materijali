//ES5
function Prefixer(prefix) {
    this.prefix = prefix;
}
Prefixer.prototype.prefixArray = function (arr) {
    // var that = this; // zbog cega nam treba ova linija koda?
    return arr.map(function (x) {
        return this.prefix + x;
    });
};

var pre = new Prefixer('Hi ');
console.log(pre.prefixArray(['Joe', 'Alex']));

//------------------------------------------------------------
//Arrow funkcije
function PrefixerA(prefix){
    this.prefix = prefix;	
}

PrefixerA.prototype.prefixArray = function (arr) {
	//this ima opseg
    return arr.map(x => this.prefix + x);
};

pre = new PrefixerA('Hi ');
console.log(pre.prefixArray(['Joe', 'Alex']));
