//iterator kroz niz
var arr = [1,2,3];
var it = arr[Symbol.iterator]();
console.log(it.next()); // { value: 1, done: false }
console.log(it.next()); // { value: 2, done: false }
console.log(it.next()); // { value: 3, done: false }
console.log(it.next()); // { value: undefined, done: true }

//custom iterator
var Fib = {
  [Symbol.iterator]() {
    
    var n1 = 1, n2 = 1;
    
    return {
      
      // make the iterator an iterable
      [Symbol.iterator]() { return this; },
      
      next() {
        var current = n2;
        n2 = n1;
        n1 = n1 + current;
        return { value: current, done: false };
      },

      return(v) {
        console.log("Fibonacci sequence abandoned.");
        return { value: v, done: true };
      }
    };
  }
};

for (var v of Fib) {
  console.log( v );
  if (v > 50) break;
}