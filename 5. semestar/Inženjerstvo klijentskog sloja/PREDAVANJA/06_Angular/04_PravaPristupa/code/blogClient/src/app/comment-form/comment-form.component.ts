import { Component, OnInit } from '@angular/core';
import { Comment } from '../model/comment';
import { Output } from '@angular/core';
import { EventEmitter } from '@angular/core';

@Component({
  selector: 'app-comment-form',
  templateUrl: './comment-form.component.html',
  styleUrls: ['./comment-form.component.css']
})
export class CommentFormComponent implements OnInit {

  comment:Comment;

  @Output()
  saveComment:EventEmitter<Comment> = new EventEmitter();

  constructor() { }

  ngOnInit() {
    this.comment = {
      text:''
    };
  }

  save(){
    this.saveComment.emit(this.comment);
    this.comment = {
      text:''
    };    
  }
}
