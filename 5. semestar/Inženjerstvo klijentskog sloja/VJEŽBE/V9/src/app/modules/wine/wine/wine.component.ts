import { Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { SharedService } from '../../shared/shared.service';
import { WineService } from '../wine.service';

@Component({
  selector: 'app-wine',
  templateUrl: './wine.component.html',
  styleUrls: ['./wine.component.css'],
})
export class WineComponent implements OnInit {
  displayedColumns: string[] = ['name', 'year', 'grapes', 'country', 'region'];
  dataSource!: MatTableDataSource<Wine>;
  wines: Wine[] = [];
  condition: boolean = true;

  valueFromCreateComponent = '';

  @ViewChild(MatPaginator) paginator!: any;
  @ViewChild(MatSort) sort!: any;

  constructor(
    private wineService: WineService,
    private sharedService: SharedService
  ) {}

  ngOnInit(): void {
    this.wineService.selectedValue$.subscribe((value) => {
      this.valueFromCreateComponent = value;
    });

    this.wineService.getAll().subscribe({
      next: (res) => {
        this.wines = res;
        this.dataSource = new MatTableDataSource<Wine>(this.wines);
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
      },
      error: (error) => {
        this.sharedService.openSnack('Ups nismo uspeli da dobavimo podatke!');
      },
    });
  }

  changeState() {
    this.condition = !this.condition;
  }
}

export interface Wine {
  _id: number;
  name: string;
  year: number;
  grapes: string;
  country: string;
  region: string;
}
