import { LiveAnnouncer } from '@angular/cdk/a11y';
import {
  AfterViewInit,
  ChangeDetectorRef,
  Component,
  OnInit,
  ViewChild,
} from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort, Sort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { WineService } from 'src/app/service/wine.service';

@Component({
  selector: 'app-wine',
  templateUrl: './wine.component.html',
  styleUrls: ['./wine.component.css'],
})
export class WineComponent implements OnInit, AfterViewInit {
  displayedColumns: string[] = ['name', 'year', 'grapes', 'country', 'region'];
  dataSource!: MatTableDataSource<Wine>;
  wines: Wine[] = [];
  condition: boolean = true;

  @ViewChild(MatPaginator) paginator!: any;
  @ViewChild(MatSort) sort!: any;

  constructor(private wineService: WineService) {
    
  }

  ngOnInit(): void {
    this.wines = this.wineService.getAll();
    this.dataSource = new MatTableDataSource<Wine>(this.wines);
  }

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  changeState() {
    this.condition = !this.condition;
  }
}

export interface Wine {
  _id: number;
  name: string;
  description: string;
  year: number;
  grapes: string;
  country: string;
  region: string;
  picture: string;
}
