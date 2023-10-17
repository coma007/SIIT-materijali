let sqrt: (x:number) => number|string = function(x:number){
    if(x>=0){
        return Math.sqrt(x);
    }
    else{
        return 'there is no sqrt';
    }
}

let a: number|string = sqrt(-2);
console.log(a);