var Point = /** @class */ (function () {
    function Point(x, y) {
        this.x = x;
        this.y = y;
        this.c = ++Point.counter;
    }
    Point.prototype.toString = function () {
        return this.x + ',' + this.y + ',' + this.c;
    };
    Point.counter = 0;
    return Point;
}());
var Point1 = Point;
Point1.counter = 100;
var p1 = new Point(100, 200);
var p2 = new Point(100, 200);
var p3 = new Point1(100, 200);
console.log(p1);
console.log(p2);
console.log(p3);
