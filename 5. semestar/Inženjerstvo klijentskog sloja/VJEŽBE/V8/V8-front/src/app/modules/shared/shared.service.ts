import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SharedService {
  private snackMessage$ = new BehaviorSubject<any>({});
  newSnackMessage$ = this.snackMessage$.asObservable();

  constructor() {}

  openSnack(message: string) {
    this.snackMessage$.next(message);
  }
}
