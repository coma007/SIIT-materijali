import { Component, OnInit } from '@angular/core';
import { Input } from '@angular/core';
import { BlogEntry } from '../model/blogEntry';
import { Output } from '@angular/core';
import { SharedBlogEntryService } from '../services/shared-blog-entry.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-blog-entry-list',
  templateUrl: './blog-entry-list.component.html',
  styleUrls: ['./blog-entry-list.component.css']
})
export class BlogEntryListComponent implements OnInit {

  @Input()
  blogEntries:BlogEntry[];

  constructor(private sharedBlogEntryService:SharedBlogEntryService,
              private router:Router) {

  }

  ngOnInit() {
  }

  details(blogEntry:BlogEntry, index:number){
    this.sharedBlogEntryService.blogEntry = blogEntry;
    this.router.navigate(['/entry',index]);
  }
}
