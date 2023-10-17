import { Observable, Subscription, IDisposable, ConnectableObservable } from "rx";
import Random from "../util/Random";

// dva pretplatnika na hladnu observablu
export default class Primer3a{

    run():void {
        let source:Observable<number> = Observable
            .range(0,3)
            .flatMap((x) => 
                Observable
                .of(x)
                .delay(Random.randomTime())//odlaganje za random vreme    
            )
            .map((x:number) => {
                console.log('obsrvable element index:',x);
                return Random.randomInt();
            });

        // konverzija hladne observable u vrucu
        let connectable:ConnectableObservable<number> = source.publish();

        let sub1:IDisposable = connectable.subscribe(
            (x:number) => {console.log('sub1:',x);},
            (err:any) => {console.log('err:',err)},
            () => {console.log('sub1 end')}
        );

        let sub2:IDisposable = connectable.subscribe(
            (x:number) => {console.log('sub2:',x);},
            (err:any) => {console.log('err:',err)},
            () => {console.log('sub2 end')}
        );

        // povezivanje vruca observabla je povezana na source i pocinje da 
        // salje vrednosti pretplatnicima
        connectable.connect();
    }
}