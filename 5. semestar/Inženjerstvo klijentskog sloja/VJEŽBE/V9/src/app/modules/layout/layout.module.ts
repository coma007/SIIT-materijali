import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from 'src/infrastructure/app-routing.module';
import { MaterialModule } from 'src/infrastructure/material.module';
import { MapModule } from '../map/map/map.module';
import { AdminNavbarComponent } from './admin-navbar/admin-navbar.component';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { NavbarComponent } from './navbar/navbar.component';
import { UserNavbarComponent } from './user-navbar/user-navbar.component';

@NgModule({
  declarations: [
    HeaderComponent,
    HomeComponent,
    NavbarComponent,
    AdminNavbarComponent,
    UserNavbarComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    MaterialModule,
    MapModule,
  ],
  exports: [HeaderComponent, NavbarComponent],
})
export class LayoutModule {}
