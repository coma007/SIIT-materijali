import { Component, OnInit, Input } from '@angular/core';
import { Wine } from '../model/wine.model';
import { WineService } from '../services/wine.service';

@Component({
  selector: 'wc-wine-list',
  templateUrl: './wine-list.component.html',
  styleUrls: ['./wine-list.component.css']
})
export class WineListComponent implements OnInit {
  private wineList: Wine[] = [];
  private totalSize: number = 0;
  private pageSize: number = 5;
  private currentPage: number = 1;

  constructor(
    private wineService: WineService
  ) {

  }

  changePage(newPage :number){
    this.currentPage = newPage;
    this.wineList = this.wineService.getAll(newPage, this.pageSize);
  }

  ngOnInit() {
    this.wineList = this.wineService.getAll(this.currentPage, this.pageSize);
    this.totalSize = this.wineService.getTotalSize();
  }
}
