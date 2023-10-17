import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { Comment } from '../../model/comment';
import { BlogEntry } from '../../model/blogEntry';
import dataBlogEntries from '../../util/dataBlogEntries';
import * as _ from 'lodash';
import searchEntries from '../../util/searchEntries'
import { BlogEntryService } from '../../services/blog-entry/blog-entry.service';
import { Observable } from 'rxjs/Observable';
import { AuthenticationService } from '../../services/authentication-service.service';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent implements OnInit {

  blogEntries: Observable<BlogEntry[]>;
  
  constructor(private blogEntryService: BlogEntryService,
              private authService: AuthenticationService) { 

  }

  ngOnInit() {
    this.blogEntries = this.blogEntryService.getAll();
  }
  
  saveBlogEntry(blogEntry: BlogEntry) {
    this.blogEntryService.save(blogEntry).subscribe( data => {
      this.filter('');
    })
    // this.blogEntriesBckup.push(blogEntry);
    // this.blogEntries = _.cloneDeep(this.blogEntriesBckup);
  }

  filter(text:string){
    this.blogEntries = this.blogEntryService.filter(text);
  }

  delete(id:any){
    console.log(id);
    this.blogEntryService.delete(id).subscribe(data =>
      this.filter('')
    );
  }

  isLoggedIn():boolean{
    return this.authService.isLoggedIn();
  }
}
