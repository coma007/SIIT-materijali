import { Observable, IDisposable } from "rx";
import Random from "../util/Random";
//concat operator
export default class Primer5{
    run():void{
        let source1:Observable<number> = Observable
        .range(0,3)
        .flatMap((x) => 
            Observable
            .of(x)
            .delay(Random.randomTime())//odlaganje za random vreme    
        )
        .map((x:number) => {console.log('obsrvable 1 element index:',x);return Random.randomInt();});

        let source2:Observable<number> = Observable
        .range(0,3)
        .flatMap((x) => 
            Observable
            .of(x)
            .delay(Random.randomTime())//odlaganje za random vreme    
        )
        .map((x:number) => {console.log('obsrvable 2 element index:',x);return Random.randomInt();});

        let source3:Observable<number> = Observable.concat(source1, source2);

        let sub:IDisposable = source3.subscribe(
            (x:number) => {console.log('sub:',x);},
            (err:any) => {console.log('err:',err)},
            () => {console.log('sub end')}
        );

    }
}