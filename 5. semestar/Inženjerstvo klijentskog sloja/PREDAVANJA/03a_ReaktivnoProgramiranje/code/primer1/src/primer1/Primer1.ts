import Random from '../util/Random';
import {Observable} from 'rx';

//map, reduce, filter
export default class Primer1{

    run():void{
        let source:Observable<number> = Observable
        .range(1,100) // range kreira observablu kao niz u datim granicama
        .flatMap((x) =>
            Observable
              .of(x)
              .delay(Random.randomTime())//odlaganje za random vreme
          )
          .filter(x => x%2==0)
          .map(x => x*2)
          .reduce((x,y) => x+y);

        source.subscribe(
            (x:number|string)=>{console.log('next:',x)},
            (err)=>{console.log('err:',JSON.stringify(err))},
            ()=>{console.log('end')}
        )
    }
}