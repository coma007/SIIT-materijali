interface IStack<T>{
    push(item: T): void;
    pop(): T;
}

class Stack<T> implements IStack<T>{
    private values: T[];
    constructor(){
        this.values = [];
    }
    push(item: T){
        this.values.push(item);
    }
    pop(){
        return this.values.pop();
    }
}

let s:Stack<String> = new Stack();
s.push('Hello');
s.push('world');
s.push('!');

console.log(s.pop());