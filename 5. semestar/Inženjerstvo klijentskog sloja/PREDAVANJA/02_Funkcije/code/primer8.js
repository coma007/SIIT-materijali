//closure i privatna svojstva

//objekat dobije vrednost koju vrati IIFE
var myObject = (function() {
  //u IIFE imamo varijablu koja se vidi iz unutrasnjih funkcija, ali ne i spolja
  var value = 0;
  //IIFE odmah vrati objekat
  return {
    //metode
    increment: function(inc) {
      //privilegovane metode imaju pristup varijabli value
      value += typeof inc === 'number' ? inc : 1;
    },
    getValue: function() {
      return value;
    }
  };
}());

myObject.increment();
//ne mozemo da pristupimo varijabli value
console.log(myObject.value);//undefined
//ali mozemo da pozovemo privilegovane metode koje mogu da pristupe varijabli
console.log(myObject.getValue());
