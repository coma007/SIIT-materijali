import { Observable, Subscription, IDisposable } from "rx";
import Random from "../util/Random";

// dva pretplatnika na hladnu observablu
export default class Primer3{

    run():void {
        let source:Observable<number> = Observable
            .range(0,3)
            .flatMap((x) => 
                Observable
                .of(x)
                .delay(Random.randomTime())//odlaganje za random vreme    
            )
            .map((x:number) => {console.log('obsrvable element index:',x);return Random.randomInt();});

        let sub1:IDisposable = source.subscribe(
            (x:number) => {console.log('sub1:',x);},
            (err:any) => {console.log('err:',err)},
            () => {console.log('sub1 end')}
        );

        let sub2:IDisposable = source.subscribe(
            (x:number) => {console.log('sub2:',x);},
            (err:any) => {console.log('err:',err)},
            () => {console.log('sub2 end')}
        );
    }
}