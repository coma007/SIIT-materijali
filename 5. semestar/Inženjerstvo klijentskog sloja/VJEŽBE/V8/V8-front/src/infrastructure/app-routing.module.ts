import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateWineReactiveComponent } from 'src/app/modules/wine-module/create-wine-reactive/create-wine-reactive.component';
import { HomeComponent } from 'src/app/modules/layout-module/home/home.component';
import { WineDetailsComponent } from 'src/app/modules/wine-module/wine-details/wine-details.component';
import { WineComponent } from '../app/modules/wine-module/wine/wine.component';
import { LoginComponent } from 'src/app/modules/auth/login/login.component';
import { LoginGuard } from 'src/app/modules/auth/guard/login.guard';

const routes: Routes = [
  { path: 'wine', component: WineComponent },
  { path: 'wine/:wineId', component: WineDetailsComponent },
  {
    path: 'home',
    component: HomeComponent,
  },
  { path: 'createReactive', component: CreateWineReactiveComponent },
  {
    path: 'login',
    component: LoginComponent,
    canActivate: [LoginGuard],
    loadChildren: () =>
      import('../app/modules/auth/auth.module').then((m) => m.AuthModule),
  },
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: '**', component: HomeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
