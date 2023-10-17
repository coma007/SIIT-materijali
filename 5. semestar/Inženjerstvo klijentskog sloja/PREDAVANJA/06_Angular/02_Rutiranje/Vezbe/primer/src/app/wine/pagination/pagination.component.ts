import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'wc-pagination',
  templateUrl: './pagination.component.html',
  styleUrls: ['./pagination.component.css']
})
export class PaginationComponent implements OnInit {
	@Input() totalItems :number;
	@Input() pageSize :number;	
  @Output() onPageSelected :EventEmitter<number>;
	pages :number[];
  activePage :number = 1;

  	constructor() { 
      this.onPageSelected = new EventEmitter();
    }

  	private getNoPages() :number{
  		return Math.ceil(this.totalItems/this.pageSize);
  	}

  	ngOnInit() {
  		this.pages = [];
  		for(let i=1; i<=this.getNoPages(); i++){
  			this.pages.push(i);
  		}
  	}

    pageSelected(newPage :number){
      if(newPage >= 1 && newPage <= this.getNoPages()){
        this.activePage = newPage;
        this.onPageSelected.emit(this.activePage);
      }  
      console.log("Active page set to: ", this.activePage);  
    }
}
