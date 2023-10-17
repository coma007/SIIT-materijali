let subtract: (x:number, y:number) => number = 
    function(x:number, y:number){
        return x-y;
    }

    let subtract1 = 
    function(x:number, y:number){
        return x-y;
    }

function choose(numbers:number):number;

function choose(numbers:number[], number):number;

function choose(numbers, index?){
    if(numbers === undefined){
        return 0;
    }
    else if(numbers instanceof Array){
        return numbers[index];
    }
    else if(!isNaN(numbers)){
        return numbers;
    }
    else{
        return 0;
    }
}

console.log(choose([1,2,3],1));
console.log(choose(100));