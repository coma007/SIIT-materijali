import { Observable, IDisposable, Subject } from "rx";
import Random from "../util/Random";
// subject primer
export default class Primer12{
    run():void{
        let source:Observable<number> = Observable // spoljasnja observabla
        .range(0,5)
        .flatMap(x => 
            Observable // unutrasnja obesrvabla unutrasnje observable
            .of(x)
            .delay(Random.randomTime())
        );

        let subject:Subject<number> = new Subject();

        let subSource:IDisposable = source.subscribe(subject);

        let sub1:IDisposable = subject.subscribe(
            (x:number) => {console.log('sub1:',x);},
            (err:any) => {console.log('err:',err)},
            () => {console.log('sub1 end')}
        );

        let sub2:IDisposable = subject.subscribe(
            (x:number) => {console.log('sub2:',x);},
            (err:any) => {console.log('err:',err)},
            () => {console.log('sub2 end')}
        );
        
    }
}