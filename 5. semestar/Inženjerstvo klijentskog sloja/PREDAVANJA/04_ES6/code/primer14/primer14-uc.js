//--"klasa"
class Foo {
  constructor(a,b) {
    this.x = a;
    this.y = b;
  }
  gimmeXY() {
    return this.x * this.y;
  }
}

var f = new Foo( 5, 15 );
console.log(f.x); // 5
console.log(f.y); // 15
console.log(f.gimmeXY()); // 75

//--"nasledjivanje"
class Bar extends Foo {
  constructor(a,b,c) {
    super( a, b );
    this.z = c;
  }
  gimmeXYZ() {
    return super.gimmeXY() * this.z;
  }
}

var b = new Bar( 5, 15, 25 );

console.log(b.x);
console.log(b.y);
console.log(b.z);
console.log(b.gimmeXYZ());
console.log(b.gimmeXY());


//--static
class Baz {
  static answer = 42;
  f() { console.log( "function call" ); }
  static cool() { console.log( "cool" ); }
}
class Buz extends Baz {
  constructor() {
  	super();
    console.log( new.target.answer );
  }
}

console.log(Baz.answer); // 42
console.log(Buz.answer); // 42
var b = new Buz(); // 42
console.log(b.f());
// console.log(b.cool()); // cool is not a function
// console.log(b.answer); // undefined -- `answer` is static on `Foo`