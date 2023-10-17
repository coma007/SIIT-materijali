import { Component, OnInit } from '@angular/core';
import { WineService } from '../services/wine.service';
import { Router, ActivatedRoute } from '@angular/router';
import { Wine } from '../model/wine.model';
import { ToastrService } from 'ngx-toastr';

@Component({
	selector: 'app-add-wine-template',
	templateUrl: './add-wine-template.component.html',
	styleUrls: ['./add-wine-template.component.scss']
})
export class AddWineTemplateComponent implements OnInit {
	wine = {};

	constructor(
		private wineService: WineService,
		private router: Router,
		private toastr: ToastrService
	) {}

	ngOnInit() {
	}

	onSubmit() {
		this.wineService.add(this.wine as Wine).subscribe(
			result => {
				this.toastr.success(result);
				this.router.navigate(['wines']);
			}
		);
	}
}
