//apply i monkey patching
//objekat koji cuva dosadasnju sracunatu vrednost
//i na nju dodaje ili oduzima nove vrednosti
var calculator = {
  value: 0,
  add: function(x){
    this.value+=x;
  },
  subtract: function (x) {
    this.value-=x;
  }
};

calculator.add(5);
console.log('calculator.value: '+calculator.value);

//hocemo da izmenimo add metodu
//tako da se dodaje dvostruka vrednost od zadate
//da bismo mogli da koristimo staru metodu, sacuvamo je u varijabli
var originalAdd = calculator.add;

//definisemo novu metodu
calculator.add = function (x) {
  //kod koji se izvrsava pre funkcije
  console.log('preparing data');
  //originalAdd pozivamo kao funkciju (ne kao metodu)
  //to znaci da je this objekat window
  //originalAdd(2*x);
  //ovaj problem zaobilazimo tako sto pozovemo originalAdd
  //pomocu apply i prosledimo joj this koji zelimo
  originalAdd.apply(this,[2*x]);
  //kod koji se izvrsava posle funkcije
  console.log('calculator.value: '+calculator.value);
};

calculator.add(5);
