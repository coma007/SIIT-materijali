var Album = /** @class */ (function () {
    function Album(title, author) {
        this.title = title;
        this.author = author;
    }
    return Album;
}());
var birthOfTheCool = new Album('birthOfTheCool', 'Miles Davis');
var a = birthOfTheCool;
var f1 = function (x) { return 100; };
var f2 = function (x, y) { return 200; };
f2 = f1;
f1 = f2; // greska!
