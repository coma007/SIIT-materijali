function mix(x, y) {
    var retVal = {};
    for (var i in x) {
        retVal[i] = x[i];
    }
    for (var i in y) {
        if (!retVal.hasOwnProperty(i)) {
            retVal[i] = y[i];
        }
    }
    return retVal;
}
var Point = /** @class */ (function () {
    function Point(x, y) {
        this.x = x;
        this.y = y;
    }
    return Point;
}());
var Message = /** @class */ (function () {
    function Message(text) {
        this.text = text;
    }
    return Message;
}());
var p = new Point(100, 200);
var m = new Message('Unexpected point!');
var messagePoint = mix(m, p);
console.log(messagePoint);
