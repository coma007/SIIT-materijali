import { Component, OnInit } from '@angular/core';
import { Input } from '@angular/core';
import { BlogEntry } from '../model/blogEntry';
import { Output } from '@angular/core';
import { SharedBlogEntryService } from '../services/shared-blog-entry.service';
import { Router } from '@angular/router';
import { EventEmitter } from '@angular/core';
import { AuthenticationService } from '../services/authentication-service.service';

@Component({
  selector: 'app-blog-entry-list',
  templateUrl: './blog-entry-list.component.html',
  styleUrls: ['./blog-entry-list.component.css']
})
export class BlogEntryListComponent implements OnInit {

  @Input()
  blogEntries:BlogEntry[];

  @Output()
  deleteBlogEntry:EventEmitter<any> = new EventEmitter();

  constructor(private sharedBlogEntryService:SharedBlogEntryService,
              private router:Router,
              private authService: AuthenticationService) {

  }

  ngOnInit() {
  }

  details(blogEntry:BlogEntry){
    this.router.navigate(['/entry/',blogEntry._id]);
  }

  delete(id:any){
    this.deleteBlogEntry.emit(id);
  }

  isLoggedIn():boolean{
    return this.authService.isLoggedIn();
  }
}
