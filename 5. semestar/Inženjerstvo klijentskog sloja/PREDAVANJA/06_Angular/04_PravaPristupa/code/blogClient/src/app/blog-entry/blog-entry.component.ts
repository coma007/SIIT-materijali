import { Component, OnInit } from '@angular/core';
import { Input } from '@angular/core';
import { BlogEntry } from '../model/blogEntry';

@Component({
  selector: 'app-blog-entry',
  templateUrl: './blog-entry.component.html',
  styleUrls: ['./blog-entry.component.css']
})
export class BlogEntryComponent implements OnInit {

  @Input()
  blogEntry:BlogEntry;

  @Input()
  showComments:boolean;

  constructor() { }

  ngOnInit() {
  }

}
