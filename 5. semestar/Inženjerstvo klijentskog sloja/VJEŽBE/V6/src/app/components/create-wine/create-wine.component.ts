import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { WineService } from 'src/app/service/wine.service';

@Component({
  selector: 'app-create-wine',
  templateUrl: './create-wine.component.html',
  styleUrls: ['./create-wine.component.css'],
})
export class CreateWineComponent implements OnInit {
  createWineForm = new FormGroup({
    name: new FormControl(),
    year: new FormControl(),
    grapes: new FormControl(),
    country: new FormControl(),
    region: new FormControl('', [Validators.required]),
  });

  constructor(private wineService: WineService, private router: Router) {}

  ngOnInit(): void {}

  create() {
    if (this.createWineForm.valid) {
      this.wineService.add(this.createWineForm.value);
      this.router.navigate(['wine']);
    }
  }
}
