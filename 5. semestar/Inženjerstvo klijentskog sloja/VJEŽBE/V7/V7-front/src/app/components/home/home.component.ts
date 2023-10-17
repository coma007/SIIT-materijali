import { Component, OnInit } from '@angular/core';
import { WineService } from 'src/app/service/wine.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  constructor(private wineService: WineService) {}
  valueFromChild = '';
  parentToChild = 'Pozdrav iz parent component';
  info = 'Pozdrav iz home component';

  ngOnInit(): void {}

  addItem(valueFromChild: string) {
    this.valueFromChild = valueFromChild;
  }

  test() {
    this.wineService.setValue(this.info);
  }
}
