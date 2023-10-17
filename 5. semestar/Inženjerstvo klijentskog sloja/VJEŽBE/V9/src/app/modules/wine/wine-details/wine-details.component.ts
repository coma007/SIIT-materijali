import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { WineService } from '../wine.service';
import { Wine } from '../wine/wine.component';

@Component({
  selector: 'app-wine-details',
  templateUrl: './wine-details.component.html',
  styleUrls: ['./wine-details.component.css'],
})
export class WineDetailsComponent implements OnInit {
  wine: Wine = {
    _id: 0,
    name: '',
    year: 0,
    grapes: '',
    country: '',
    region: '',
  };

  constructor(
    private route: ActivatedRoute,
    private wineService: WineService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.wineService
        .getWine(+params['wineId'])
        .subscribe((wine) => (this.wine = wine));
    });
  }
}
