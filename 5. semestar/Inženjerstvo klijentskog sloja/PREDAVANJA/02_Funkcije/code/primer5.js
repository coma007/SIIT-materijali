//izmena osnovnih tipova
var x = {
  value:0
};

//proverimo da li je neko vec promenio objekat
if (!Object.prototype.sayHello) {
  //dodajemo metodu u prototip
  Object.prototype.sayHello = function() {
    console.log('hallo world');
  };
}

//promena se odrazava na citva lanac "naslednika"
x.sayHello();
