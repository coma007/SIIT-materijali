import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BlogEntry } from '../../model/blogEntry';
import { Observable } from 'rxjs/Observable';
import { HttpParams } from '@angular/common/http';
import { Comment } from '../../model/comment';

@Injectable()
export class BlogEntryService {

  private readonly path = "/api/blogEntries";

  constructor(private http: HttpClient) { }

  getAll():Observable<BlogEntry[]> {
    return this.http.get<BlogEntry[]>(this.path); 
  }

  filter(entryText:string):Observable<BlogEntry[]> {
    const params:HttpParams = new HttpParams().set('entry',entryText);
    // let params:HttpParams = new HttpParams();
    // params = params.append('entry',entryText);
    // params = params.append('bla','blabla');
    return this.http.get<BlogEntry[]>(this.path,{params}); 
  }
  
  get(id:any):Observable<BlogEntry>{
    // const params: HttpParams = new HttpParams().set('_id',id);
    return this.http.get<BlogEntry>(this.path+`/${id}`);
  }

  save(blogEntry:BlogEntry){
    return this.http.post(this.path,blogEntry);
  }

  delete(id:any){
    return this.http.delete(this.path+`/${id}`);
  }

}
