import { Component, OnInit } from '@angular/core';
import { Wine } from '../model/wine.model';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { validateStefanNameFactory } from '../validators/custom-validator';
import { Router } from '@angular/router';
import { WineService } from '../services/wine.service';

@Component({
  selector: 'app-add-wine-reactive',
  templateUrl: './add-wine-reactive.component.html',
  styleUrls: ['./add-wine-reactive.component.css']
})
export class AddWineReactiveComponent implements OnInit {
  wine :Wine;
	wineForm :FormGroup;

  	constructor(
			private fb: FormBuilder,
			private router: Router,
			private wineService: WineService
		) { 
  		this.createForm();
  	}

  	ngOnInit() {}

  	createForm(){
  		this.wineForm = this.fb.group({
  			'name': ["", [Validators.required, Validators.minLength(2), validateStefanNameFactory()]],
  			'year': ["", Validators.required],
  			'grapes': ["", Validators.required],
  			'country': ["", Validators.required],
  			'region': ["", Validators.required],
  			'description': ["", Validators.required]
  		});
  	}

  	onSubmit(){
  		this.wine = new Wine(this.wineForm.value);
			// console.log(this.wine);
			this.wineService.add(this.wine);  		
			this.wineForm.reset();
			this.router.navigate(['wines']);
  	}

}
