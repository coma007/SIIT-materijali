import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing/app-routing.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HeaderComponent } from './core/header/header.component';
import { NavbarComponent } from './core/navbar/navbar.component';
import { WineListComponent } from './wine/wine-list/wine-list.component';
import { SearchFormComponent } from './wine/search-form/search-form.component';
import { PaginationComponent } from './wine/pagination/pagination.component';
import { TableComponent } from './wine/table/table.component';
import { AddWineTemplateComponent } from './wine/add-wine-template/add-wine-template.component';
import { AddWineReactiveComponent } from './wine/add-wine-reactive/add-wine-reactive.component';
import { StefanNameValidatorDirective } from './directives/stefan-name-validator.directive';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    NavbarComponent,
    WineListComponent,
    SearchFormComponent,
    PaginationComponent,
    TableComponent,
    AddWineTemplateComponent,
    AddWineReactiveComponent,
    StefanNameValidatorDirective
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
