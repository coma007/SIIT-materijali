var x = 5;
var y = [1, 2, 3];
// var y: number[] = [1,2,'aaa'];
var z = [1, 2, 'hello', true];
var Color;
(function (Color) {
    Color[Color["Red"] = 3] = "Red";
    Color[Color["Green"] = 4] = "Green";
    Color[Color["Blue"] = 5] = "Blue";
})(Color || (Color = {}));
;
var c = Color.Green;
// var u:any = 5;
var u = 5;
// var u:number = 5;
u = 'asdf';
var v;
// var v: undefined|null;
v = undefined;
v = null;
function error(message) {
    throw new Error(message);
}
var s = 'ovo je neki tekst';
s.length;
