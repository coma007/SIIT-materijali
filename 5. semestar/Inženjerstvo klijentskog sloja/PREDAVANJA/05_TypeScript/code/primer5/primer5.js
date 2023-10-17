var subtract = function (x, y) {
    return x - y;
};
var subtract1 = function (x, y) {
    return x - y;
};
function choose(numbers, index) {
    if (numbers === undefined) {
        return 0;
    }
    else if (numbers instanceof Array) {
        return numbers[index];
    }
    else if (!isNaN(numbers)) {
        return numbers;
    }
    else {
        return 0;
    }
}
console.log(choose([1, 2, 3], 1));
console.log(choose(100));
