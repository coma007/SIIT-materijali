import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Wine } from '../components/wine/wine.component';

@Injectable({
  providedIn: 'root',
})
export class WineService {
  private value$ = new BehaviorSubject<any>({});
  selectedValue$ = this.value$.asObservable();

  constructor(private http: HttpClient) {}

  setValue(test: any) {
    this.value$.next(test);
  }

  getAll(): Observable<Wine[]> {
    return this.http.get<Wine[]>(environment.apiHost + 'wines');
  }

  getWine(wineId: number): Observable<Wine> {
    return this.http.get<Wine>(environment.apiHost + 'wines/' + wineId);
  }

  addReactive(wine: any): Observable<any> {
    const options: any = {
      responseType: 'text',
    };
    return this.http.post<string>(environment.apiHost + 'add', wine, options);
  }

  add(wine: any): Observable<any> {
    const options: any = {
      responseType: 'text',
    };

    return this.http.post<string>(
      environment.apiHost + 'add',
      {
        name: wine.name,
        year: wine.year,
        grapes: wine.grapes,
        country: wine.country,
        region: wine.region,
      },
      options
    );
  }
}
