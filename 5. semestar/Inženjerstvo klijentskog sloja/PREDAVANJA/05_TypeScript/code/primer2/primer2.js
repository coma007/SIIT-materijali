var Point = /** @class */ (function () {
    function Point(x, y, z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    Point.prototype.show = function () {
        console.log('(x:', this.x, ', y:', this.y, ', z:', this.z, ')');
    };
    return Point;
}());
var a = new Point(100, 200, 300);
a.show();
var b = {
    x: 100,
    y: 200,
    z: 300,
    u: 400,
    show: function () {
        console.log('(x:', this.x, ', y:', this.y, ', z:', this.z, ', u:', this.u, ')');
    }
};
b.show();
var bb = {
    x: 100,
    y: 200,
    z: 300,
    show: function () {
        console.log('(x:', this.x, ', y:', this.y, ', z:', this.z, ')');
    }
};
