import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from '../infrastructure/app-routing.module';
import { AppComponent } from './app.component';
import { WineComponent } from './components/wine/wine.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from 'src/infrastructure/material.module';
import { NavbarComponent } from './components/navbar/navbar.component';
import { HeaderComponent } from './components/header/header.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import { HomeComponent } from './components/home/home.component';
import { CreateWineComponent } from './components/create-wine/create-wine.component';
import { FormsModule, NgModel, ReactiveFormsModule } from '@angular/forms';
import { WineService } from './service/wine.service';
import { NewExampleComponent } from './new-example/new-example.component';

@NgModule({
  declarations: [
    AppComponent,
    WineComponent,
    NavbarComponent,
    HeaderComponent,
    HomeComponent,
    CreateWineComponent,
    NewExampleComponent,
  ],
  imports: [
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    FlexLayoutModule,
    ReactiveFormsModule,
  ],
  exports: [
    
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
