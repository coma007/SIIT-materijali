import { Routes } from '@angular/router';

import { WineListComponent } from '../wine/wine-list/wine-list.component';
import { AddWineTemplateComponent } from '../wine/add-wine-template/add-wine-template.component';
import { AddWineReactiveComponent } from '../wine/add-wine-reactive/add-wine-reactive.component';

export const routes :Routes = [
	{path: 'wines', component: WineListComponent},
	{path: 'wines/add', component: AddWineTemplateComponent}
];
