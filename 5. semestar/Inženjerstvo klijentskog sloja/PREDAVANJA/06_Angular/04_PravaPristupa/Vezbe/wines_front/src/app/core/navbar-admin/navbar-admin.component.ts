import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/wine/services/authentication.service';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';

@Component({
	selector: 'app-navbar-admin',
	templateUrl: './navbar-admin.component.html',
	styleUrls: ['./navbar-admin.component.scss']
})
export class NavbarAdminComponent implements OnInit {

	constructor(
		private authenticationService: AuthenticationService,
		private toastr: ToastrService,
		private router: Router
	) { }

	ngOnInit() {
	}

	logout() {
		this.authenticationService.logout().subscribe(
			result => {
				localStorage.removeItem('user');
				this.toastr.success(result);
				this.router.navigate(['login']);
			},
			error => {
				this.toastr.error(error.error);
			}
		);
	}

}
