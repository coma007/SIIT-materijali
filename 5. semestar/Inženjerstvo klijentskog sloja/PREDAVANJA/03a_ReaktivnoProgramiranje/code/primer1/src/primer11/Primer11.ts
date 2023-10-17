import { Observable, IDisposable } from "rx";
import Random from "../util/Random";
// concatMap primer
export default class Primer11{
    run():void{
        let source:Observable<number> = Observable // spoljasnja observabla
        .range(0,5)
        .concatMap(x => 
            Observable // unutrasnja observabla
            .range(0,x)
            .concatMap(x => 
                Observable // unutrasnja obesrvabla unutrasnje observable
                .of(x)
                .delay(Random.randomTime())
            )
            .delay(Random.randomTime())
        );

        let sub:IDisposable = source.subscribe(
            (x:number) => {console.log('sub:',x);},
            (err:any) => {console.log('err:',err)},
            () => {console.log('sub end')}
        );

    }
}