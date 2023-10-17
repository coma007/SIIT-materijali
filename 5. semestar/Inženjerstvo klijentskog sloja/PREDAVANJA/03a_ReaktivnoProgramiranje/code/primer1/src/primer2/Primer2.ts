import Random from "../util/Random";
import { Observable } from "rx";

// array vs observable
export default class Primer2{
    
    static readonly arr:number[] = Array(1000000) // prazan niz od milion elemenata
                                    .fill(1) // popunjavanje praznog niza jedinicama (od ES6)
                                    .map(() => Random.randomInt());

    private static benchmarkArray():number{
        const start:number = performance.now();
        const result:number = Primer2.arr
            .map(x => x*2).map(x => x*3).map(x => x-2).map(x => x+1).map(x => x+3)
            .filter(x => x>0).reduce((x,y) => x+y);
        const stop:number = performance.now();
        return stop - start;
    }

    private static benchmarkObservable():number{
        const start:number = performance.now();
        var result:number = null; 
        Observable.from(Primer2.arr) // from operator kreira observablu od niza
            .map(x => x*2).map(x => x*3).map(x => x-2).map(x => x+1).map(x => x+3)
            .filter(x => x>0).reduce((x,y) => x+y).subscribe(x => result = x);
        const stop:number = performance.now();
        return stop - start;
    }


    run():void {
        console.log('array:',Primer2.benchmarkArray());
        console.log('observable:',Primer2.benchmarkObservable());
    }
}