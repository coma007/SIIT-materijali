//Generator
function *foo() {
  while (true) {
    var x = yield Math.random();
    console.log('x:',x);
  }
}

var it = foo();

for (var i = 0; i < 10; i++) {
  var v = it.next(i);
  console.log('v:',v);  
};

//--Delegiranje yield iteratoru
function *bar() {
  yield *[1,2,3];
}

it = bar();

for (i = 0; i < 4; i++) {
  v = it.next();
  console.log('v:',v);  
};
