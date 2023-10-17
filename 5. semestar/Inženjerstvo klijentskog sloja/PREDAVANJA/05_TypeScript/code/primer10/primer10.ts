function mix <T, U> (x:T, y:U):T&U{
    let retVal:T&U = {} as T&U;
    for(let i in x){
        (<any>retVal)[i] = (<any>x)[i];
    }
    for(let i in y){
        if(!retVal.hasOwnProperty(i)){
            (<any>retVal)[i] = (<any>y)[i];
        }
    }
    return retVal;
}

class Point{
    constructor(public x:number, public y:number){}
}

class Message{
    constructor(public text: string){}
}

let p = new Point(100,200);
let m = new Message('Unexpected point!');
let messagePoint:Message&Point = mix<Message, Point>(m,p);
console.log(messagePoint);

