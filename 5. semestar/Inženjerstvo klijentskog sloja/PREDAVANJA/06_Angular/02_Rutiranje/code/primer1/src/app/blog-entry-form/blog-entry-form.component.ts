import { Component, OnInit } from '@angular/core';
import { BlogEntry } from '../model/blogEntry';
import { Output } from '@angular/core';
import { EventEmitter } from '@angular/core';

@Component({
  selector: 'app-blog-entry-form',
  templateUrl: './blog-entry-form.component.html',
  styleUrls: ['./blog-entry-form.component.css']
})
export class BlogEntryFormComponent implements OnInit {

  @Output()
  saveBlogEntryEvent = new EventEmitter<BlogEntry>()

  newBlogEntry:BlogEntry;

  // username:string = '';

  constructor() { }

  ngOnInit() {
    this.newBlogEntry={
      title:'',
      description:'',
      entry:'',
      comments:[]
    }
  }

  save(){
    this.newBlogEntry.date = new Date();
    this.saveBlogEntryEvent.emit(this.newBlogEntry);
    this.newBlogEntry={
      title:'',
      description:'',
      entry:'',
      comments:[]
    }
  }
}
