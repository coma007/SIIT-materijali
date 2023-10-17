import { Observable, IDisposable } from "rx";
import Random from "../util/Random";
// mergeMap primer
export default class Primer10{
    run():void{
        let source:Observable<number> = Observable // spoljasnja observabla
        .range(0,5)
        .flatMap(x => 
            Observable // unutrasnja observabla
            .range(0,x)
            .flatMap(x => 
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