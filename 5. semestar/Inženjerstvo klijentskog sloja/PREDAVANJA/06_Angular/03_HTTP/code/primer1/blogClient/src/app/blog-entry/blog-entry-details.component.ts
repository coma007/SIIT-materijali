import { Component, OnInit } from '@angular/core';
import { Input } from '@angular/core';
import { BlogEntry } from '../model/blogEntry';
import { BlogEntryComponent } from './blog-entry.component';
import { SharedBlogEntryService } from '../services/shared-blog-entry.service';
import { ActivatedRoute } from '@angular/router';
import { BlogEntryService } from '../services/blog-entry/blog-entry.service';
import { Observable } from 'rxjs/Observable';
import { CommentService } from '../services/comment/comment.service';

@Component({
  selector: 'app-blog-entry-details',
  templateUrl: './blog-entry.component.html',
  styleUrls: ['./blog-entry.component.css']
})
//posto su veoma slicne BlogEntry i BlogEntryDetails recikliraju isti templejt
//BlogEntryDetails nasledjuje BlogEntry i time preuzima i njene impute
export class BlogEntryDetailsComponent extends BlogEntryComponent {

  sub:any;

  index:number;

  private id;

  blogEntry:BlogEntry;
  //kompomente BlogEntry i BlogEntryDetails komuniciraju kroz servis
  constructor(private blogEntryService: BlogEntryService,
              private commentService: CommentService,
              private route: ActivatedRoute) {
    super();
   }

  ngOnInit() {
    // this.blogEntry = this.sharedBlogEntryService.blogEntry;
    this.sub = this.route.params.subscribe(params => {
      // postavljanje observable narusilo bi api nasledjene klase
      // zbog toga je observabla razresena i postavljena vrednost 
      // blogEntry$ = this.blogEntryService.get(+params['id']); 
      this.id = params['id'];
      this.loadData();
    });
  }

  loadData(){
    this.blogEntryService.get(this.id).subscribe(data => {
      this.blogEntry = data;
    });  
  }

  saveComment(comment:Comment){
    console.log(comment);
    this.commentService.save(comment, this.id).subscribe( data =>{
        this.loadData();
      }
    );
  }

}
