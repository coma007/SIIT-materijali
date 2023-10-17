import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/wine/services/authentication.service';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';

@Component({
	selector: 'app-navbar-user',
	templateUrl: './navbar-user.component.html',
	styleUrls: ['./navbar-user.component.scss']
})
export class NavbarUserComponent implements OnInit {

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
