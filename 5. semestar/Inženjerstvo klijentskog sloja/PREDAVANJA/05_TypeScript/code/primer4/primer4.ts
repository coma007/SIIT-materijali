class Point{
    x:number;
    y:number;
    c:number;
    static counter:number = 0;
    constructor(x:number, y:number){
        this.x = x;
        this.y = y;
        this.c = ++Point.counter;
    }
    toString(){
        return this.x+','+this.y+','+this.c;
    }
}

let Point1: typeof Point = Point;
Point1.counter = 100;

let p1 = new Point(100,200);
let p2 = new Point(100,200);
let p3 = new Point1(100,200);

console.log(p1);
console.log(p2);
console.log(p3);