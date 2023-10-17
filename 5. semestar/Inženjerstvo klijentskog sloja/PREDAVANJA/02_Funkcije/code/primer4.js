//funkcija prima neogranicen broj parametara
var multiply = function () {
  var i;
  var result = 1;
  for(i=0;i<arguments.length;i++){
    if (typeof arguments[i] !== 'number') {
      throw {
        name: 'TypeError',
        message: 'multiply is defined on numbers'
      }
    }
    result *= arguments[i];
  }
  return result;
};

var factorial5;
try{
  factorial5 = multiply(5,4,'3',2);
  console.log(factorial5);
}catch(e){
  console.log(JSON.stringify(e));
}
