function logClass(target: any) {
    //referenca na originalni  
    //konstruktor
    var original = target;

    //pomoćna funkcija
    //generise instancu klase
    function construct(cstr, args) {
        var c: any = function () {
            return cstr.apply(this, args);
        }
        c.prototype = cstr.prototype;
        return new c();
    }
    //novi konstruktor
    //loguje instanciranje 
    //i instancira objekat
    var f: any = function (...args) {
        console.log("New: " + original.name);
        return construct(original, args);
    }

    f.prototype = original.prototype;

    return f;
}

@logClass
class Person { 

  public name: string;
  public surname: string;

  constructor(name : string, surname : string) { 
    this.name = name;
    this.surname = surname;
  }
}

//prilikom instanciranja ispisaće se 
//u konzolu new "new Person"
var p = new Person("Pera", "Peric");
console.log(p);
