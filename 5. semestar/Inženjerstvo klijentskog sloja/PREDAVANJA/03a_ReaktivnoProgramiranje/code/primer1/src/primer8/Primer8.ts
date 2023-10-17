import { Observable, IDisposable } from "rx";
import Random from "../util/Random";
// debounce operator
export default class Primer8{
    run():void{
        let source:Observable<number> = Observable
        .range(0,10)
        .flatMap((x) => 
            Observable
            .of(x)
            .delay(Random.randomTime())//odlaganje za random vreme    
        )
        .map((x:number) => {console.log('obsrvable 1 element index:',x);return Random.randomInt();})
        .debounce(50);

        let sub:IDisposable = source.subscribe(
            (x:number) => {console.log('sub:',x);},
            (err:any) => {console.log('err:',err)},
            () => {console.log('sub end')}
        );

    }
}