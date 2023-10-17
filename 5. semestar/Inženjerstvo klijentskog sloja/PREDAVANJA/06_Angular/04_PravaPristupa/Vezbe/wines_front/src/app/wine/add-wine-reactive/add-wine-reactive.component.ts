import { Component, OnInit } from '@angular/core';
import { Wine } from '../model/wine.model';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { validateTestFactory } from '../validators/custom-validator';
import { Router, ActivatedRoute } from '@angular/router';
import { WineService } from '../services/wine.service';
import { ToastrService } from 'ngx-toastr';

@Component({
	selector: 'app-add-wine-reactive',
	templateUrl: './add-wine-reactive.component.html',
	styleUrls: ['./add-wine-reactive.component.scss']
})
export class AddWineReactiveComponent implements OnInit {
 	wine: Wine;
	wineForm: FormGroup;
	number: number;

	constructor(
			private fb: FormBuilder,
			private router: Router,
			private wineService: WineService,
			private route: ActivatedRoute,
			private toastr: ToastrService
		) {
		this.createForm();
	}

	ngOnInit() {
		this.number = this.route.snapshot.params.broj as number;
	}

	createForm() {
		this.wineForm = this.fb.group({
			'name': ['', [Validators.required, Validators.minLength(2), validateTestFactory()]],
			'year': ['', Validators.required],
			'grapes': ['', Validators.required],
			'country': ['', Validators.required],
			'region': ['', Validators.required],
			'description': ['', Validators.required]
		});
	}

	onSubmit() {
		console.log(this.number);
		this.wine = this.wineForm.value;
		this.wineService.add(this.wine as Wine).subscribe(
			result => {
				this.toastr.success(result);
				this.router.navigate(['wines']);
			}
		);
		this.wineForm.reset();
		this.router.navigate(['wines']);
	}
}
