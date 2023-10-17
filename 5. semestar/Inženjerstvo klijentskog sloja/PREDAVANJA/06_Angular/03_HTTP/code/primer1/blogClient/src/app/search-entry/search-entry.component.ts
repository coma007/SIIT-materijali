import { Component, OnInit } from '@angular/core';
import { EventEmitter } from '@angular/core';
import { Output } from '@angular/core';

@Component({
  selector: 'app-search-entry',
  templateUrl: './search-entry.component.html',
  styleUrls: ['./search-entry.component.css']
})
export class SearchEntryComponent implements OnInit {

  @Output()
  filterEntriesEvent:EventEmitter<string> = new EventEmitter();

  filterText:string;

  constructor() { }

  ngOnInit() {
    this.filterText='';
  }

  filter(){
    this.filterEntriesEvent.emit(this.filterText);
  }

  reset(){
    this.filterText='';
    this.filter();
  }
}
