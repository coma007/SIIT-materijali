interface Book{
    title: string;
    author: string;
}

class Album{
    title: string;
    author: string;
    constructor(title:string, author:string){
        this.title = title;
        this.author = author;
    }
}

let birthOfTheCool: Album = new Album('birthOfTheCool','Miles Davis');
let a: Book = birthOfTheCool;

let f1: ((x: string) => number) = (x: string) => 100;
let f2: ((x: string, y: boolean) => number) = (x: string, y: boolean) => 200;

f2 = f1;
// f1 = f2;// greska!