var c1 = {
    createdAt: 'Sun Nov 19 2017 20:16:14',
    text: 'tekst komentara',
    comments: []
};
var c2 = {
    createdAt: 'Sun Nov 19 2017 20:16:14',
    text: 'tekst komentara',
    comments: [],
    related: ['http://www.example.org/comments/123321']
};
console.log(c1);
console.log(c2);
var a = { x: 100, y: 200, z: 400, u: '[1,2,3]' };
console.log(a);
var myFilter = function (list, term) {
    return list.filter(function (item) {
        return item.indexOf(term) != -1;
    });
};
console.log(myFilter(['foo', 'bar', 'baz'], 'ba'));
// interface IPoint {
//     readonly x: number;
//     readonly y: number;
//     //proizvoljan broj polja tipa string ili broj
//     [propName: string]: string | number;
// }
var a1 = { x: 1, y: 2, z: 3, u: 4 };
console.log(a1);
//# sourceMappingURL=primer1.js.map