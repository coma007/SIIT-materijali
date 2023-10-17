import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { yearRangeValidator } from '../custom-validator/custom-validator';
import { WineService } from '../wine.service';

@Component({
  selector: 'app-create-wine-reactive',
  templateUrl: './create-wine-reactive.component.html',
  styleUrls: ['./create-wine-reactive.component.css'],
})
export class CreateWineReactiveComponent implements OnInit {
  createWineForm = new FormGroup({
    name: new FormControl('Test'),
    year: new FormControl(null, yearRangeValidator),
    grapes: new FormControl(),
    country: new FormControl(),
    region: new FormControl('', [Validators.required]),
  });

  constructor(private wineService: WineService, private router: Router) {}

  ngOnInit(): void {}

  add() {
    if (this.createWineForm.valid) {
      this.wineService
        .addReactive(this.createWineForm.value)
        .subscribe((res: any) => {
          this.router.navigate(['wine']);
        });
    }
  }
}
