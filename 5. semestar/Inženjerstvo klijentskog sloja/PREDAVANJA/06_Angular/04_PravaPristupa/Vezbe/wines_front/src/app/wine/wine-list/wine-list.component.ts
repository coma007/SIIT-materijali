import { Component, OnInit, Input } from '@angular/core';
import { Wine } from '../model/wine.model';
import { WineService } from '../services/wine.service';

@Component({
	selector: 'app-wine-list',
	templateUrl: './wine-list.component.html',
	styleUrls: ['./wine-list.component.scss']
})
export class WineListComponent implements OnInit {
	pageSize: number;
	currentPage: number;
	totalSize: number;
	wineList: Wine[];

	constructor(
		private wineService: WineService
	) {
		this.pageSize = 5;
		this.currentPage = 1;
		this.totalSize = 1;
	}

	changePage(newPage: number) {
		this.wineService.getAll(newPage - 1, this.pageSize).subscribe(
			res => {
				this.wineList = res.body as Wine[];
				this.totalSize = Number(res.headers.get('Total-pages'));
			}
		);
	}

	ngOnInit() {
		this.wineService.getAll(this.currentPage - 1, this.pageSize).subscribe(
			res => {
				this.wineList = res.body as Wine[];
				this.totalSize = Number(res.headers.get('Total-pages'));
			}
		);
	}
}
