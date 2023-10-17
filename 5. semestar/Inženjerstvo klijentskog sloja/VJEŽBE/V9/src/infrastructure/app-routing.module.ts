import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginGuard } from 'src/app/modules/auth/guard/login.guard';
import { HomeComponent } from 'src/app/modules/layout/home/home.component';
import { CreateWineReactiveComponent } from 'src/app/modules/wine/create-wine-reactive/create-wine-reactive.component';
import { WineDetailsComponent } from 'src/app/modules/wine/wine-details/wine-details.component';
import { WineComponent } from 'src/app/modules/wine/wine/wine.component';

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
