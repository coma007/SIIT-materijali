interface IComment {
	createdAt?:string;
	updatedAt?:string;
	signedBy?:string;
	text:string;
	//kolekcija komentara
    comments?: IComment[];
}

let c1: IComment = {
    createdAt: 'Sun Nov 19 2017 20:16:14',
    text: 'tekst komentara',
    comments: []
}

let c2: IComment = {
    createdAt: 'Sun Nov 19 2017 20:16:14',
    text: 'tekst komentara',
    comments: [],
    related: ['http://www.example.org/comments/123321']
} as IComment;

console.log(c1);
console.log(c2);

interface IPoint {
    readonly x: number;
    readonly y: number;
    //proizvoljan broj polja tipa string ili broj
    [propName: string]: string | number;
}

let a:IPoint = { x:100, y:200, z:400, u:'[1,2,3]' };
console.log(a);

// interfejs funkcije
interface IFilterFunction {
    (sourceList: string[], subString: string): string[];
  }

let myFilter: IFilterFunction = function (list: string[], term: string) {
    return list.filter(function (item) {
        return item.indexOf(term)!=-1;
    });
}

console.log(myFilter(['foo', 'bar', 'baz'], 'ba'));

interface IPoint3D extends IPoint{
    z: number;
}

// interface IPoint {
//     readonly x: number;
//     readonly y: number;
//     //proizvoljan broj polja tipa string ili broj
//     [propName: string]: string | number;
// }

let a1: IPoint3D = { x: 1, y: 2, z: 3, u:4 };

console.log(a1);

//interfejsi se mogu prosirivati naknadno i 
//interfejsi se ne hoistuju
interface IPoint3D{
    u: number;
}