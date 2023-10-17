var x: number = 5;
var y: Array<number> = [1,2,3];
// var y: number[] = [1,2,'aaa'];
var z: [number, number, string, boolean] = [1,2, 'hello', true];
enum Color {Red=3, Green, Blue};
var c: Color = Color.Green; 
// var u:any = 5;
var u:number|string = 5;
// var u:number = 5;
u = 'asdf';
var v: void;
// var v: undefined|null;
v = undefined;
v = null;

function error(message: string): never {
    throw new Error(message);
}

var s: any = 'ovo je neki tekst';
(<string>s).length;
(s as string).length;