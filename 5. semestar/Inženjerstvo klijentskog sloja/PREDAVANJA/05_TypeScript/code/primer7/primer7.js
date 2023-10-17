var Stack = /** @class */ (function () {
    function Stack() {
        this.values = [];
    }
    Stack.prototype.push = function (item) {
        this.values.push(item);
    };
    Stack.prototype.pop = function () {
        return this.values.pop();
    };
    return Stack;
}());
var s = new Stack();
s.push('Hello');
s.push('world');
s.push('!');
console.log(s.pop());
