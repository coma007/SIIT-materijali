export default class Random{

    private static readonly MAX_TIME:number = 1200;

    private static readonly MIN_TIME:number = 400;

    private static readonly MAX_INT:number = -2;

    private static readonly MIN_INT:number = 4;

    static randomTime:() => number = () => Math.random() * (Random.MAX_TIME - Random.MIN_TIME) + Random.MIN_TIME;
    
    static randomInt:() => number = () => Math.floor(Math.random() * (Random.MAX_INT - Random.MIN_INT) + Random.MIN_INT);

    constructor(){

    }
}