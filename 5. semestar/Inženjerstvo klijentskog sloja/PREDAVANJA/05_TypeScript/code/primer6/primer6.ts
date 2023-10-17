// λx.x
function identity<T>(x:T): T {
    return x;
}

console.log(identity<String>('Hello world'));