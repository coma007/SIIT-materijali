import { Injectable } from '@angular/core';
import { Comment } from '../../model/comment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { BlogEntry } from '../../model/blogEntry';

@Injectable()
export class CommentService {

  private readonly path:string = "/api/comments";

  constructor(private http:HttpClient) { }

  save(comment:Comment, blogEntryId:any):Observable<BlogEntry>{
    return this.http.post<BlogEntry>(this.path+`/blogEntry/${blogEntryId}`, comment);
  }

}
