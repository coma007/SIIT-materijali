import { Injectable } from '@angular/core';
import { Router, ActivatedRouteSnapshot, CanActivate } from '@angular/router';
import { AuthenticationService } from '../wine/services/authentication.service';
import { JwtHelperService } from '@auth0/angular-jwt';

@Injectable({
	providedIn: 'root'
})
export class RoleGuard implements CanActivate {

	constructor(
		public auth: AuthenticationService,
		public router: Router
	) { }

	canActivate(route: ActivatedRouteSnapshot): boolean {
		const expectedRoles: string = route.data.expectedRoles;
		const token = localStorage.getItem('user');
		const jwt: JwtHelperService = new JwtHelperService();

		if (!token) {
			this.router.navigate(['/login']);
			return false;
		}

		const info = jwt.decodeToken(token);
		const roles: string[] = expectedRoles.split('|', 2);

		if (roles.indexOf(info.role[0].authority) === -1) {
			this.router.navigate(['/wines']);
			return false;
		}
		return true;
	}
}
