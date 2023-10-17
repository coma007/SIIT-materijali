let x: number = 5;


let y: number[];
let z: Array<number>;

let x1: [string, string, number] = ['Pera','Peric',123321];
enum Color {Red = 1, Green, Blue};
let x2: Color;

let x3: any;
let x4: void;
x4 = undefined;
x4 = null;
// x4 = 5;

let x5:never;

let f: (x: number, y:number) => number = function(x:number, y:number){
    return x+y;
}

function f1(x: number, y: number): number{
    return x+y;
}
let x6:any = 'asdf';

let x7:string = x6 as string;
// let x7:string = <string>x6;

interface Osoba{
    readonly ime:string;
    prezime:string;
    JMBG:number;
    brojIndeksa?:string;
}

let o1: Osoba = {
    ime:'Pera',
    prezime:'Peric',
    JMBG:123321,
    brojIndeksa: 'e123'
}

let o2: Osoba = {
    ime:'Marko',
    prezime:'Markovic',
    JMBG:321123
}

// o1.ime = 'Jovan';




o1 = o2;

interface Point {
    readonly x: number;
    readonly y: number;
    [propName: string]: number;
}

let p1: Point = {
    x:5,
    y:10,
    z:15
}