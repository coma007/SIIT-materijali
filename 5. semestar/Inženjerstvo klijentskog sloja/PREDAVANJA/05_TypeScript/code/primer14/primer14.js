var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
function logClass(target) {
    //referenca na originalni  
    //konstruktor
    var original = target;
    //pomoćna funkcija
    //generise instancu klase
    function construct(cstr, args) {
        var c = function () {
            return cstr.apply(this, args);
        };
        c.prototype = cstr.prototype;
        return new c();
    }
    //novi konstruktor
    //loguje instanciranje 
    //i instancira objekat
    var f = function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i] = arguments[_i];
        }
        console.log("New: " + original.name);
        return construct(original, args);
    };
    f.prototype = original.prototype;
    return f;
}
var Person = /** @class */ (function () {
    function Person(name, surname) {
        this.name = name;
        this.surname = surname;
    }
    Person = __decorate([
        logClass
    ], Person);
    return Person;
}());
//prilikom instanciranja ispisaće se 
//u konzolu new "new Person"
var p = new Person("Pera", "Peric");
console.log(p);
