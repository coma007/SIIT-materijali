//modul
//brojac koji vrati autoinkrementiranu vrednost
var counterMaker = function () {
  //privatno svojstvo
  var current = 0;
  return{
    //privilegovana funkcija
    getCounter : function () {
      current += 1;
      return current;
    }
  };
};

var counter = counterMaker();

var x1 = {
  'id':counter.getCounter()
};
var x2 = {
  'id':counter.getCounter()
};
var x3 = {
  'id':counter.getCounter()
};

console.log(JSON.stringify(x1), JSON.stringify(x2), JSON.stringify(x3));
