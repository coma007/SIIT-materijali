import { Observable, IDisposable } from "rx";
import Random from "../util/Random";
// takeUntil operator
export default class Primer9{
    run():void{
        let timer:Observable<number> = Observable.timer(1000);
        
        let source:Observable<number> = Observable
        .range(0,10)
        .flatMap((x) => 
            Observable
            .of(x)
            .delay(Random.randomTime())//odlaganje za random vreme    
        )
        .map((x:number) => {console.log('obsrvable 1 element index:',x);return Random.randomInt();})
        .takeUntil(timer);

        let sub:IDisposable = source.subscribe(
            (x:number) => {console.log('sub:',x);},
            (err:any) => {console.log('err:',err)},
            () => {console.log('sub end')}
        );

    }
}