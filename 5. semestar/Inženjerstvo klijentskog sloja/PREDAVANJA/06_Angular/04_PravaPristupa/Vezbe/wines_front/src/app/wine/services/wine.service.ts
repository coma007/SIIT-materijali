import { Injectable } from '@angular/core';
import { Wine } from '../model/wine.model';
import { HttpClientModule, HttpParams, HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
	providedIn: 'root'
})
export class WineService {
	private headers = new HttpHeaders({'Content-Type': 'application/json'});

	constructor(
		private http: HttpClient
	) {}

	getAll(page: number, size: number): Observable<any> {
		let queryParams = {};

		queryParams = {
			headers: this.headers,
			observe: 'response',
			params: new HttpParams()
				.set('page', String(page))
				.append('size', String(size)),
		};

		return this.http.get('api/getAll', queryParams);
	}

	add(newWine: Wine): Observable<any> {
		return this.http.post('api/add', newWine, {headers: this.headers, responseType: 'text'});
	}
}
