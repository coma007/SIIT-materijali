//memoizacija
//funkcija dobije vrednost koju vrati IIFE
var fibonacci = (function() {
  //niz zapamcenih vrednosti je privatni
  var memo = [0, 1];
  var fib = function(n) {
    //funkcija prvo proba da nadje vec izracunatu vrednost u nizu
    var result = memo[n];
    //ukoliko ne uspe racuna je rekurzivno
    if (typeof result !== 'number') {
      result = fib(n - 1) + fib(n - 2);
      //i doda u niz
      memo[n] = result;
    }
    return result;
  };
  return fib;
}());

// varijanta bez memoizacije
var fibonacciBM = function(n) {
  return n < 2 ? n : fibonacciBM(n - 1) + fibonacciBM(n - 2);
};

console.log(fibonacci(50));
