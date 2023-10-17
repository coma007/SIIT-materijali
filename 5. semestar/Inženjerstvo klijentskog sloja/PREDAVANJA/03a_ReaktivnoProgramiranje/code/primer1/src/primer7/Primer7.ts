import { Observable, IDisposable } from "rx";
import Random from "../util/Random";
// throw operator
export default class Primer7{
    run():void{
        let source:Observable<any> = Observable.throw(new Error('There are no numbers'));

        let example:Observable<any> = source.catch(err => 
            Observable.of(`error ${err}`)
        );

        let sub:IDisposable = example.subscribe(
            (x:number) => {console.log('sub:',x);}
        );

    }
}