interface IPoint {
    x: number;
    y: number;
    show():void;
}

class Point implements IPoint{
    x: number;
    y: number;
    z: number;
    constructor(x: number, y: number, z:number) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    show() {
        console.log('(x:', this.x, ', y:', this.y, ', z:', this.z, ')');
    }
}

let a = new Point(100, 200, 300);
a.show();

interface IPoint4D extends Point{
    u:number;
}

let b:IPoint4D = {
    x:100,
    y:200,
    z:300,
    u:400,
    show(){
        console.log('(x:', this.x, ', y:', this.y, ', z:', this.z, ', u:', this.u, ')');        
    }
}

b.show();

let bb:Point = {
    x:100,
    y:200,
    z:300,
    show(){
        console.log('(x:', this.x, ', y:', this.y, ', z:', this.z, ')');        
    }
}
