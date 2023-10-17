import { Component, OnInit, Input, Output, EventEmitter, OnChanges } from '@angular/core';
import { UtilService } from '../services/util.service';

@Component({
	selector: 'app-pagination',
	templateUrl: './pagination.component.html',
	styleUrls: ['./pagination.component.scss']
})
export class PaginationComponent implements OnInit, OnChanges {
	@Input() totalItems: number;
	@Input() pageSize: number;
	@Output() pageSelected: EventEmitter<number>;
	pages: number[];
	activePage: number;

	constructor(
		private utilService: UtilService
	) {
		this.pageSelected = new EventEmitter();
		this.activePage = 1;
	}

	ngOnInit() {
		this.pages = [];
		for (let i = 1; i <= this.utilService.getNoPages(this.totalItems, this.pageSize); i++) {
			this.pages.push(i);
		}
	}

	ngOnChanges(changes) {
		this.totalItems = changes.totalItems.currentValue;
		this.pages = [];
		for (let i = 1; i <= this.utilService.getNoPages(this.totalItems, this.pageSize); i++) {
			this.pages.push(i);
		}
	}

	selected(newPage: number) {
		if (newPage >= 1 && newPage <= this.utilService.getNoPages(this.totalItems, this.pageSize)) {
			this.activePage = newPage;
			this.pageSelected.emit(this.activePage);
		}
	}
}
