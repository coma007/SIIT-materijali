import { Observable, IDisposable } from "rx";
import Random from "../util/Random";

// generator fibonacijevih brojeva
function* fibonacci ():IterableIterator<number> {
    var fn1 = 1;
    var fn2 = 1;
    while (true){
      var current = fn2;
      fn2 = fn1;
      fn1 = fn1 + current;
      yield current;
    }
  }
// observabla generatora
export default class Primer4{
    run():void {
        let source:Observable<any> = Observable
        .from(fibonacci());
        
        let sub1:IDisposable = source.subscribe(
            (x:number) => {console.log('sub:',x);},
            (err:any) => {console.log('err:',err)},
            () => {console.log('sub end')}
        );

    }
}