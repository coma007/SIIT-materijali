import { Routes } from '@angular/router';

import { WineListComponent } from '../wine/wine-list/wine-list.component';
import { AddWineTemplateComponent } from '../wine/add-wine-template/add-wine-template.component';
import { AddWineReactiveComponent } from '../wine/add-wine-reactive/add-wine-reactive.component';
import { LoginComponent } from '../wine/login/login.component';
import { LoginGuard } from '../guards/login.service';
import { RoleGuard } from '../guards/role.service';

export const routes: Routes = [
	{
		path: 'wines',
		component: WineListComponent,
		canActivate: [RoleGuard],
		data: {expectedRoles: 'ADMIN|WINE_USER'}
	},
	{
		path: 'wines/add',
		component: AddWineTemplateComponent,
		canActivate: [RoleGuard],
		data: {expectedRoles: 'ADMIN'}
	},
	{
		path: 'wines/add/:number',
		component: AddWineReactiveComponent,
		canActivate: [RoleGuard],
		data: {expectedRoles: 'ADMIN'}
	},
	{
		path: 'login',
		component: LoginComponent,
		canActivate: [LoginGuard]
	}
];
