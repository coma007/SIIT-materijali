import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing/app-routing.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HeaderComponent } from './core/header/header.component';
import { WineListComponent } from './wine/wine-list/wine-list.component';
import { PaginationComponent } from './wine/pagination/pagination.component';
import { TableComponent } from './wine/table/table.component';
import { AddWineTemplateComponent } from './wine/add-wine-template/add-wine-template.component';
import { AddWineReactiveComponent } from './wine/add-wine-reactive/add-wine-reactive.component';
import { CustomValidatorDirective } from './directives/custom-validator.directive';
import { TestPipe } from './pipes/test.pipe';
import { LoginComponent } from './wine/login/login.component';

import { ToastrModule } from 'ngx-toastr';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavbarAdminComponent } from './core/navbar-admin/navbar-admin.component';
import { NavbarUserComponent } from './core/navbar-user/navbar-user.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { Interceptor } from './interceptors/intercept.service';

@NgModule({
	declarations: [
		AppComponent,
		HeaderComponent,
		WineListComponent,
		PaginationComponent,
		TableComponent,
		AddWineTemplateComponent,
		AddWineReactiveComponent,
		CustomValidatorDirective,
		TestPipe,
		LoginComponent,
		NavbarAdminComponent,
		NavbarUserComponent
	],
	imports: [
		BrowserModule,
		AppRoutingModule,
		FormsModule,
		ReactiveFormsModule,
		BrowserAnimationsModule, // required animations module
		ToastrModule.forRoot(),
		HttpClientModule
	],
	providers: [{provide: HTTP_INTERCEPTORS, useClass: Interceptor, multi: true}],
	bootstrap: [AppComponent]
})
export class AppModule { }
