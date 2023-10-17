class C{
    static x:number = 10;
    y:number;
    constructor(y:number){
        this.y = y;
    }
}

let c1:C = new C(15);
console.log(C.x);
// console.log(c1.x);