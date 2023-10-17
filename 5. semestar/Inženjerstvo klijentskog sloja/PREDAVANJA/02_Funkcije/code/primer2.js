// Konstruktor
var Counter = function (count) {
  this.count = count;
};
// metode
Counter.prototype.increment = function(val){
  this.count += !val?1:val;
};
Counter.prototype.getCount = function () {
  return this.count;
};
//kreniranje objekata
//svaki objekat ima count i metode increment i getCount
var c1 = new Counter(5);
var c2 = new Counter(10);
//pozivi metoda
c1.increment();
c2.increment(2);
console.log('c1.getCount(): '+c1.getCount());//6
console.log('c2.getCount(): '+c2.getCount());//12

//Apply
//counterHolder ce biti this u apply metodi
var counterHolder = {
  count: 15
};
//pozivamo increment funkciju nad counterHolder-om sa argumentom 5
Counter.prototype.increment.apply(counterHolder,[5]);
console.log('counterHolder.count: '+counterHolder.count);
